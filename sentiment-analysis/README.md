# Applying a Sentiment Analysis model on movie review data.

This projects shows how to use a trained ML model from Layer to infer a sentiment score on movie review data.

To use this project, you must add a `my-bigquery` profile in your `~/.dbt/profiles.yaml` that configures the access to BigQuery and the Layer-specific configuration entries for `type` and `project`. 

This is a sample entry:

```
my-bigquery:
  target: dev
  outputs:
    dev:
      type: layer_bigquery
      method: service-account
      project: <Your BigQuery project here>
      dataset: <Your BigQuery dataset here>
      threads: 1
      keyfile: <Path to the GCP keyfile>
      layer_project: <Name of the Layer project>
```
