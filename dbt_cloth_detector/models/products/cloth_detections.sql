{{ config(materialized='table') }}

SELECT
       p.id as product_id,
       layer.predict("layer/clothing/models/detector", [p.image]) as objects
FROM
     {{ ref("products") }} as p
