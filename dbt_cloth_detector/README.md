# Layer Cloth Detector

This DBT project extracts the cloth objects in a product image with using a computer vision model from [Layer](https://app.layer.ai/layer/clothing/).

## How to use

First install Layer and the required libraries

```shell
pip install layer -U -q
git clone https://github.com/ultralytics/yolov5
pip install -rv yolov5/requirements.txt
```

And seed the sample [products table](seeds/products.csv) with some random product and product images from Amazon

```shell
dbt seed
```

And finally you can run the project:

```shell
dbt run
```
