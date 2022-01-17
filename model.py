import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import metrics , preprocessing
from scipy import stats

def predict_class(features):

    train_path = 'C:\\Users\\Mounika\\Documents\\Flinkhub\\deploy\\train.csv'
    train_df = pd.read_csv(train_path)
    train_df = train_df.drop('id',axis=1)

    train_df["target"] = train_df["target"].astype('category')
    train_df["target"] = train_df["target"].cat.codes

    z = np.abs(stats.zscore(train_df))
    threshold = 7
    train_O = train_df[(z<threshold).all(axis=1)] 
    train_y = train_O['target']
    train_x = train_O.drop(['target'],axis=1)
    lm = linear_model.LogisticRegression(multi_class='multinomial',solver='lbfgs',max_iter=100)
    lm.fit(train_x, train_y)
    
    predictions = lm.predict(features) 

    return predictions


