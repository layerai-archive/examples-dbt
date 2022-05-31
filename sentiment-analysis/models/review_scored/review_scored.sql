{{ config(
		materialized='table',
		entrypoint='predict.py'
	) 
}}

SELECT review,  
layer.predict("'layer/sentiment-analysis/models/tensorflow-sentiment-analysis:3.2'", ARRAY[review_tokenized]) as review_score
from {{ref('review_categories')}}
