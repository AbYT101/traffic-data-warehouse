-- Define raw_data model
-- Extract data from input file
SELECT *
FROM {{ ref('source_pNEUMA_data') }};
