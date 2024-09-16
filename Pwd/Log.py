import pandas as pd
data=pd.read_csv('passwords.csv')

from sklearn.preprocessing import LabelEncoder
lbl=LabelEncoder()
data['password']=lbl.fit_transform(data['password'])


X=data.iloc[:,:1].values
y=data.iloc[:,-1:].values


import numpy as np
from sklearn.impute import SimpleImputer
imp=SimpleImputer(missing_values=np.nan,strategy='mean')
imp.fit(X[:,:1])
X[:,:1]=imp.transform(X[:,:1])  # import numpy as np

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)


from sklearn.ensemble import RandomForestClassifier
reg=RandomForestClassifier(n_estimators=100, random_state=42)
reg.fit(X_train,y_train.ravel())
reg.score(X_train,y_train.ravel())


def pred(x):
    arr=np.array(x).reshape(-1,1)
    p=reg.predict(arr)
    return p