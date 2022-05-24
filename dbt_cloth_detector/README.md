# Layer Cloth Detector

This DBT project extracts the cloth objects in a product image with using a computer vision model from [Layer](https://app.layer.ai/layer/clothing/).

## How to run

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

Once the project is run, Layer will fetch the product image urls from the `ref('products')` and detect the objects in that
product image. The detected objects will be saved in a new model called [cloth_detections](models/products/cloth_detections.sql) as a comma sperated values like `shirt,trousers,shoes`

## Computer Vision Model

We are using a YOLOv5 model trained with a custom dataset. You can check the following notebook to see how this model
works and how to make predictions with it:

https://colab.research.google.com/drive/1I9U7Q02d5BXCTmVO-JLWYsKeIL7Mug9p

