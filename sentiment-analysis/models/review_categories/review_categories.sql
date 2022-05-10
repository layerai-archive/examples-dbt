SELECT review,  
CASE 
	WHEN sentiment = 'positive' THEN 1
	WHEN sentiment = 'negative' THEN 0
	ELSE -1
END as sentiment_score	
from {{source('imdb_reviews','reviews')}} 