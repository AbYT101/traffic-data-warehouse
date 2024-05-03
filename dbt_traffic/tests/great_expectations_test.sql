-- Check if all required columns are present in the vehicle table
SELECT
    COUNT(*) AS num_columns
FROM
    information_schema.columns
WHERE
    table_name = 'vehicle'
    AND column_name IN ('track_id', 'type', 'traveled_d', 'avg_speed')
    AND table_schema = 'public'
    AND is_nullable = 'NO';

-- Check if the primary key column is unique in the vehicle table
SELECT
    COUNT(*) AS num_records,
    COUNT(DISTINCT track_id) AS num_unique_track_ids
FROM
    vehicle;

-- Check if speed values in vehicle_path table are within a 120km/h reasonable range
SELECT
    COUNT(*) AS num_out_of_range_speeds
FROM
    vehicle_path
WHERE
    speed < 0 OR speed > 120; 



-- Check if there are any NULL values in the lat and lon columns in vehicle_path table
SELECT
    COUNT(*) AS num_null_lat_lon
FROM
    vehicle_path
WHERE
    lat IS NULL OR lon IS NULL;

-- Check if the traveled_d values in the vehicle table are non-negative
SELECT
    COUNT(*) AS num_negative_traveled_d
FROM
    vehicle
WHERE
    traveled_d < 0;

-- Check if the time values in the vehicle_path table are increasing monotonically for each track_id
SELECT
    COUNT(*) AS num_non_monotonic_time_values
FROM (
    SELECT
        track_id,
        time,
        LAG(time) OVER (PARTITION BY track_id ORDER BY time) AS prev_time
    FROM
        vehicle_path
) AS subquery
WHERE
    time < prev_time;
