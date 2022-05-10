SELECT review,  
predict("layer/sentiment-analysis/models/imdb_data_tokenizer:1.1", ARRAY[review]) as review_tokenized
from {{ref('review_categories')}}