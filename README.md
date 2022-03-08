# TagUp Coding Challenge 👨‍💻
For TagUp's take home interview challenge

## Approach
- [x] I implemented a REST API skeleton with Flask route decorators, and specifying the accepted REST verbs with the `methods=` kwarg 
- [x] Added docstrings to standardize each function's readability and allow a new user to more easily understand the code
- [x] Dockerfile is included

Details from the TagUp challenge README
------------------------

## Technical Requirements

Please implement a basic web application that collects sensor data and reports statistics. Your server should have four routes:
- `POST /data` should accept JSON documents in the request body, with the form
    `[{"sensor": <str: sensor_id>, "timestamp": <str: iso 8601 timestamp>, "value": <float>}, ...]`
  - The sensor id is a string describing the sensor that generated the data. A single request can include data from multiple sensors.
  - The timestamp is an ISO 8601 string indicating when the data was collected. Timestamps may be represented in local time where the data is captured.
  - Value is the sensor value, represented in floating point.
- `GET /statistics/<sensor id>` should return a JSON document in the response body of the form 
  `{"last_measurement": <str: iso 8601 timestamp>, "count": <int>,
  "avg": <float>}`. 
    - the `last_measurement` value should be the time of the last measurement posted to `/data` (the time included in the request body, *not* the time the request was made)
    - the `count` value should be the total number of measurements received by the server.
    - the `avg` value should be the arithmetic average of all values received for the sensor by the server.
- `DELETE /statistics/<sensor id>` should clear any statistics for the sensor with the given ID, and the response should not include a body.
- `GET /healthz` should return a 204 response with no body if the server is ready to receive requests, and an error response (e.g. 400) otherwise.

Sample data that could be sent to `POST /data` or received from `GET /statistics/sensor1` is provided in the `samples` directory.

The server should be implemented in Python. You may use whatever web framework you are comfortable in (e.g. Flask or FastAPI). The server should be containerized using Docker. For the purposes of this exercise, you do not need to persist data to a database; the `GET` route only needs to capture measurements received since the server was started.

## Deliverable

Please share your submission as a link to a github repository containing your source code. If you do not have a github account, please create one. The github repository can be public or private; if private, please invite the following github users to collaborate:
- [wrvb](https://github.com/wrvb)
- [jtgarrity](https://github.com/jtgarrity)

Your code should be containerized using docker. Please include a `Dockerfile` that installs your dependencies and executes your server, listening for requests on port 8080. That is, we should be able to use the following commands to run your web application and access it at `localhost:8080`:
```
docker build -t exercise:latest .
docker run --rm -it -p 8080:8080 exercise:latest
```

If your submission includes any functionality not captured in the docker image (such as tests, static analysis, or sphinx-like documentation that must be built separately) please describe the functionality in a README.md file at the root of your repository.
