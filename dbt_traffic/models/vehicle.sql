-- vehicle.sql
-- This model represents a vehicle in the dataset.
-- It includes information about the vehicle type, distance traveled, and average speed.


CREATE TABLE vehicle (
    track_id SERIAL PRIMARY KEY,
    type VARCHAR,
    traveled_d FLOAT,
    avg_speed FLOAT
);
