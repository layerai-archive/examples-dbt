select Age, layer.predict("layer/titanic/models/survival_model:4.8", ARRAY[Pclass, Sex, Age, SibSp, Parch, Fare]) from {{ref('passenger_features')}} as passenger_features_prediction
