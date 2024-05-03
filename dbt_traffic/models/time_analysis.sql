
WITH journey_time AS (
    SELECT
        vp.track_id,
        SUM(vp.time) AS total_time
    FROM
        vehicle_path vp
    GROUP BY
        vp.track_id
)

SELECT
    track_id,
    total_time
FROM
    journey_time;
