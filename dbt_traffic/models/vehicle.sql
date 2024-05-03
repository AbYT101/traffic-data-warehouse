-- vehicle.sql
-- This model represents a vehicle in the dataset.
-- It includes information about the vehicle type, distance traveled, and average speed.

-- vehicle.sql

{{ docs(vehicle) }}
This model represents a vehicle in the dataset.
It includes information about the vehicle type, distance traveled, and average speed.

{{ docs(track_id) }}
A unique identifier for each vehicle.

{{ docs(type) }}
The type or category of the vehicle.

{{ docs(traveled_d) }}
The distance traveled by the vehicle.

{{ docs(avg_speed) }}
The average speed of the vehicle.



CREATE TABLE vehicle (
    track_id SERIAL PRIMARY KEY,
    type VARCHAR,
    traveled_d FLOAT,
    avg_speed FLOAT
);
