# Sentiment Analysis in DBT Dag

In this tutorial, we will see how to make multi-language sentiment analysis.

```sql
select id,
       review,
       layer.predict("layer/nlptown/models/sentimentanalysis", ARRAY[review])
from {{ref('reviews')}}
```


## How to run

First install Layer and the required libraries

```shell
pip install layer -U -q
```

And seed the sample product reviews from Amazon
```shell
dbt seed
```

And finally you can run the project:
```shell
dbt run
```