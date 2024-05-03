-- vehicle_path.sql
-- Model representing individual points along a vehicle's path.
-- This model stores data about latitude, longitude, speed, acceleration, and time.

{{ docs(vehicle_path) }}
This model represents individual points along a vehicles path.
It contains data such as latitude, longitude, speed, acceleration, and time.

{{ docs(id) }}
A unique identifier for each point along the vehicles path.

{{ docs(track_id) }}
The identifier of the vehicles track to which this point belongs.

{{ docs(lat) }}
The latitude coordinate of the vehicles location.

{{ docs(lon) }}
The longitude coordinate of the vehicles location.

{{ docs(speed) }}
The speed of the vehicle at this point along the path.

{{ docs(lon_acc) }}
The longitudinal acceleration of the vehicle at this point along the path.

{{ docs(lat_acc) }}
The lateral acceleration of the vehicle at this point along the path.

{{ docs(time) }}
The timestamp of when this point along the path was recorded.


CREATE TABLE vehicle_path (
    id SERIAL PRIMARY KEY,
    track_id INTEGER REFERENCES vehicle(track_id),
    lat FLOAT,
    lon FLOAT,
    speed FLOAT,
    lon_acc FLOAT,
    lat_acc FLOAT,
    time FLOAT
);
