# Sentiment Analysis in DBT Dag

In this tutorial, we will see how to make multi-language sentiment analysis inside DBT Dag with a simple sql like:

```sql
select id,
       review,
       layer.predict("layer/nlptown/models/sentimentanalysis", ARRAY[review])
from {{ref('reviews')}}
```

## How to run

First install the open-source [Layer DBT Adapter](https://github.com/layerai/dbt-adapters). Right now, we only support Bigquery (more to come soon)

```shell
pip install dbt-layer-bigquery -U -q
```

And install the required libraries. This ML model is a finetuned Pytorch model opensourced by [NLPTown](https://www.nlp.town/). So we need some additional libraries for Pytorch.

```shell
pip install torch torchvision
```

Add a new bigquery profile to your [DBT profile](https://docs.getdbt.com/dbt-cli/configure-your-profile/). Name it as `layer-profile`, and don't forget to set `type: layer_bigquery` for Layer to work. Here is a sample profile:


```yaml
layer-profile:
  target: dev
  outputs:
    dev:
      type: layer_bigquery
      method: service-account
      project: [GCP project id]
      dataset: [the name of your dbt dataset]
      threads: [1 or more]
      keyfile: [/path/to/bigquery/keyfile.json]
```

Clone this repo:
```shell
git clone https://github.com/layerai/examples-dbt
cd sentiment_analysis
```

And seed the sample [reviews table](seeds/reviews.csv) which includes random multi-language product reviews from Amazon.

```shell
dbt seed
```

And finally you can run the project:

```shell
dbt run
```

Once the project is run, Layer will fetch the reviews from `ref('products')` and classify the review from 1 to 5.


## Model

In this DBT example, we use a Bert model finetuned on product reviews in six languages: English, Dutch, German, French, Spanish and Italian. It predicts the sentiment of the review as a number of stars (between 1 and 5).

This model is intended for direct use as a sentiment analysis model for product reviews in any of the six languages above, or for further finetuning on related sentiment analysis tasks.


To learn more about this machine learning model:

https://app.layer.ai/layer/nlptown