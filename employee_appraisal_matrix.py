# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 17:24:05 2019

@author: shuvs
"""



import pandas as pd
import seaborn as sns

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score


df = pd.read_csv('treedata.csv')

X = df[['CreativeOpinion','OnsiteProject', 'Initiative', 'TotalProjectTaken',
        'RegularReport', 'ClientDeal', 'NonAdherenceOfPolicies']].as_matrix()
y = df['Appraisal']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

cls_svc = SVC(kernel='linear')
cls_svc.fit(X_train, y_train)



sns.pairplot(df,hue='Appraisal', palette='Dark2')

predictions = cls_svc.predict(X_test)
print(predictions)

print(confusion_matrix(y_test, predictions))
print(f1_score(y_test, predictions))
print(accuracy_score(y_test, predictions))

def yesorno(co,op,i,tp,rr,cd,nap):
    if(cls_svc.predict([[co,op,i,tp,rr,cd,nap]]))!=1:
        print('You\'re not appraised!')
    else:
        print('You\'re appraised!')



while(1):
    a = input()
    b = input()
    c = input()
    d = input()
    e = input()
    f = input()
    g = input()

    yesorno(a, b, c, d, e, f, g)
