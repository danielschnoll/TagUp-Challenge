import os
from flask import Flask, request, jsonify

app = Flask(__name__)
dataArr = []


'''
/data
requires: POST request with json data in the body, structured like the following
          [{"sensor": <str: sensor_id>, "timestamp": <str: iso 8601 timestamp>, "value": <float>}, ...]
modifies: global dataArr
throws:   None
returns:  a json response with status 200
'''
@app.route('/data', methods=["POST"])
def data():
    req = request.get_json()
    global dataArr
    dataArr += req
    return jsonify("SERVER: Data has been received")


'''
/statistics
requires: GET request with <sid> in the URL in the format sensorN, where N := {0,1,2...}
          DELETE request with <sid> in the URL in the format sensorN, where N := {0,1,2...}
modifies: global dataArr
throws:   None
returns:  GET
          json response with <sid> data, and a status 
          - 201 if the data IS NOT present for <sid>
          - 202 if the data IS present for <sid>
          DELETE
          No body response, and a status
          - 203 upon successful deletion
'''
@app.route('/statistics/<sid>', methods=["GET", "DELETE"])
def statistics(sid):
    global dataArr
    if request.method == "GET":
        # define our values
        sid = sid.strip()
        ret = {}
        count, value = 0, 0

        # get the latest <sid> stored in dataArr
        for data in reversed(dataArr):
            if data["sensor"] == sid:
                ret["last_measurement"] = data["timestamp"]
                break
        
        # aggregate all data from dataArr for <sid> 
        for data in dataArr:
            if data["sensor"] == sid:
                count += 1
                value += data["value"]

        # return 201 if sensor data is not present, otherwise return 202
        if "last_measurement" not in ret:
            ret["last_measurement"] = None
            ret["count"] = 0
            ret["avg"] = 0
            return jsonify(ret), 201
        else:
            ret["avg"] = round(value / count, 1)
            ret["count"] = count
            return jsonify(ret), 202

    # remove all elements in dataArr that have sensor of <id>
    elif request.method == "DELETE":
        newList = []
        for i in range(len(dataArr)):
            if dataArr[i]["sensor"] != sid:
                newList.append(dataArr[i])
        dataArr = newList
        return '', 203

    # Defends against bad request attempts, should be impossible to reach unless route methods arr is not defined
    else:
        return jsonify("{0} not allowed".format(request.method)), 500


'''
/healthz
requires: GET request to the URL
modifies: None
throws:   404 if server is faulty
returns:  No body response, status of 204 for healthy server
'''
@app.route('/healthz', methods = ["GET"])
def health():
    try:
        return ('', 204)
    except:
        return ('', 404)
