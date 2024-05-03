WITH vehicle_metrics AS (
    SELECT
        v.track_id,
        v.type,
        COUNT(vp.id) AS num_points,
        SUM(vp.speed) AS total_speed,
        AVG(vp.speed) AS avg_speed,
        MAX(vp.speed) AS max_speed,
        MIN(vp.speed) AS min_speed,
        MAX(vp.traveled_d) AS max_distance_traveled
    FROM
        vehicle v
    LEFT JOIN
        vehicle_path vp ON v.track_id = vp.track_id
    GROUP BY
        v.track_id, v.type
)

SELECT
    track_id,
    type,
    num_points,
    total_speed,
    avg_speed,
    max_speed,
    min_speed,
    max_distance_traveled
FROM
    vehicle_metrics;
