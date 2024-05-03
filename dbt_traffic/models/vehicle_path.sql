-- vehicle_path.sql
-- Model representing individual points along a vehicle's path.
-- This model stores data about latitude, longitude, speed, acceleration, and time.


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
