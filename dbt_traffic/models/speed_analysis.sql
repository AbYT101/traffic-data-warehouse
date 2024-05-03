WITH speed_stats AS (
    SELECT
        vp.track_id,
        AVG(vp.speed) AS avg_speed,
        MAX(vp.speed) AS max_speed,
        MIN(vp.speed) AS min_speed
    FROM
        vehicle_path vp
    GROUP BY
        vp.track_id
)

SELECT
    track_id,
    avg_speed,
    max_speed,
    min_speed
FROM
    speed_stats
