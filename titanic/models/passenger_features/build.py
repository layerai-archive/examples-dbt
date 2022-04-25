import pandas as pd

def clean_sex(sex):
    result = 0
    if sex == "female":
        result = 0
    elif sex == "male":
        result = 1
    return result


def clean_age(data):
    age = data[0]
    pclass = data[1]
    if pd.isnull(age):
        if pclass == 1:
            return 37
        elif pclass == 2:
            return 29
        else:
            return 24
    else:
        return age


def build_features(df):
    df['Sex'] = df['Sex'].apply(clean_sex)
    df['Age'] = df[['Age', 'Pclass']].apply(clean_age, axis=1)
    return df.drop(["PassengerId", "Name", "Cabin", "Ticket", "Embarked"], axis=1)


def main(dataframe):
    """
    Takes in pandas dataframe of the selected columns
    Returns a pandas dataframe of the resulting data
    """
    return build_features(dataframe)
