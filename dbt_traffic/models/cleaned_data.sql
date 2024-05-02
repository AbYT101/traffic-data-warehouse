-- Define cleaned_data model
-- Perform data cleaning and preprocessing
WITH cleaned_data AS (
    SELECT
        track_id,
        vehicle_type,
        distance_traveled_meters,
        average_speed_kmh,
        time,
        latitude,
        longitude,
        speed_kmh / 3.6 AS speed_ms, -- Convert speed from km/h to m/s
        longitudinal_acceleration,
        lateral_acceleration
    FROM {{ ref('raw_data') }}
    WHERE -- Add filtering conditions if necessary
)
SELECT *
FROM cleaned_data;
