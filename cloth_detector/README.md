# Cloth Detection in DBT Dag

![Layer Cloth Detector](assets/layer_cloth_detector.png)

This DBT project shows how to extract the cloth information in product images with a simple sql inside DBT Dag like:

```sql
SELECT
    id,
    layer.predict("layer/clothing/models/objectdetection", ARRAY[image])
FROM
    {{ ref("products") }}
```

## How it works?

We introduce a special SQL function called `layer.predict()` as you can see above. With this function, you can fetch any ML model from Layer and apply it to your data inside the DBT Dag. When you run the above sql:
1. Layer fetches the `products` table with the required `id` and `image` columns from your BigQuery.
2. Layer fetches [this computer vision model](https://app.layer.ai/layer/clothing) from Layer as requested in the predict function with `layer/clothing/models/objectdetection`
3. Layer reads all the images from products table and extract what's in the image and return it to DBT to store the extracted information in your BigQuery.



## How to run

First install the open-source [Layer DBT Adapter](https://github.com/layerai/dbt-adapters). Right now, we only support Bigquery (more to come soon)

```shell
pip install dbt-layer-bigquery -U -q
```

And install the required libraries. This ML model is a fine-tuned YOLOv5 model, so we have to install the required libraries for YOLOv5 to run.

```shell
git clone https://github.com/ultralytics/yolov5
pip install -r yolov5/requirements.txt
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
cd cloth_detector
```

And seed the sample [products table](seeds/products.csv) with some random product and product images from Amazon

```shell
dbt seed
```

And finally you can run the project:

```shell
dbt run
```

Once the project is run, Layer will fetch the product image urls from the `ref('products')` and detect the objects in that
product image. The detected objects will be saved in a new model called [cloth_detections](models/products/cloth_detections.sql) as a comma sperated values like `shirt,trousers,shoes` in your BigQuery database.

## Computer Vision Model

We are using a YOLOv5 model trained with a custom dataset. 

You can check the following notebook to see how this model
works and how to make predictions with it:

https://colab.research.google.com/drive/1I9U7Q02d5BXCTmVO-JLWYsKeIL7Mug9p

Here is a link to the Layer project if you want to learn more about this model:

https://app.layer.ai/layer/clothing
