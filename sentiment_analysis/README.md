# Sentiment Analysis in DBT Dag

In this tutorial, we will see how to make multi-language sentiment analysis.

```sql
select id,
       review,
       layer.predict("layer/nlptown/models/sentimentanalysis", ARRAY[review])
from {{ref('reviews')}}
```


## How to run

First install the DBT Layer Adapter

```shell
pip install dbt-layer-bigquery -U -q
```

And seed the sample product reviews from Amazon
```shell
dbt seed
```

And finally you can run the project:
```shell
dbt run
```