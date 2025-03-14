import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score # 정확도 함수
from catboost import CatBoostClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import csv
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

rf = RandomForestClassifier(max_features='sqrt', max_leaf_nodes=200)
lgbm = LGBMClassifier(n_estimators=100, max_depth=12, num_leaves=25, verbosity=0, min_child_samples=30)
cat = CatBoostClassifier(iterations=200, depth=7, learning_rate=0.1, l2_leaf_reg=40, verbose=0)
et = ExtraTreesClassifier(max_depth=7, max_features=None)

rank = 'DIAMOND'
result = {}
for min in range(5, 16):
    resultFilePath = f'../Dataset/perMinuteDataset/result/accuracy/{rank}.csv'
    data = pd.read_csv(f'../Dataset/preProcessed/{rank}.csv')

    X = data[data.columns.difference(['result'])]
    y = data['result']

    # # features/target, train/test dataset 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42) # 학습데이터와 평가데이터의 비율을 8:2 로 분할|
    y_train = y_train.values.ravel()
    modelList = [rf, lgbm, cat, et]
    modelNameList = ["RandomForest", "LightGBM", "CatBoost", "ExtraTree"]
    fieldnames = ["Minute", "Model", "accuracy_score", "F1_score", "ROC_AUC", "TN", "FP", "FN", "TP"]
    for i in range(4):
        model = modelList[i]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42) # 학습데이터와 평가데이터의 비율을 8:2 로 분할|
        model.fit(X_train, y_train)
        pre = model.predict(X_test)
        accuracy = round(accuracy_score(y_test, pre)*100, 2)
        f1 = round(f1_score(y_test, pre)*100, 2)
        roc_auc = round(roc_auc_score(y_test, pre)*100, 2)
        tn, fp, fn, tp = confusion_matrix(y_test, pre).ravel()
        print(f"{modelNameList[i]} Accuracy : ", accuracy, "%")
        print(f"{modelNameList[i]} f1 :", f1, "%")
        print(f"{modelNameList[i]} ROC_AUC :", roc_auc, "%")
        print('tn:', tn, ' fp:', fp, ' fn:', fn, ' tp:', tp)

        result = {"Minute": min, 
                  "Model": f"{modelNameList[i]}", 
                  "accuracy_score" : accuracy,
                  "F1_score" : f1,
                  "ROC_AUC" : roc_auc,
                  "TN": tn,
                  "FP": fp,
                  "FN": fn,
                  "TP": tp}
        # result = pd.DataFrame(result, index = [0])
        # result.to_csv(resultFilePath, index=False)
        with open(resultFilePath, 'a', newline='') as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            if min == 5 and i == 0:
                w.writeheader()
            w.writerow(result)