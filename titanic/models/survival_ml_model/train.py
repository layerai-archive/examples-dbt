import layer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np


def train(df):
    test_size = 0.3
    random_state = 42
    n_estimators = 100

    layer.log({
        "test_size": test_size,
        "random_state" : random_state,
        "n_estimators": n_estimators,
    })

    X = df.drop(["Survived"], axis=1)
    y = df["Survived"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    random_forest = RandomForestClassifier(n_estimators=n_estimators)
    random_forest.fit(X_train, y_train)
    return random_forest


def main(dataframe):
    """
    Takes in pandas dataframe of the selected columns
    Returns a trained model
    """
    return train(dataframe)


# TESTING

def dummy_passengers():
    return pd.DataFrame(
        {'PassengerId': 2,
         'Pclass': 1,
         'Name': ' Mrs. John',
         'Sex': 'female',
         'Age': 38.0,
         'SibSp': 1,
         'Parch': 0,
         'Ticket': 'PC 17599',
         'Fare': 71.2833,
         'Embarked': 'C',
         }, index=[0])


if __name__ == '__main__':
    main(dummy_passengers())
