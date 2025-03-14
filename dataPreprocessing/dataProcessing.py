import numpy as np
import pandas as pd
import warnings; warnings.filterwarnings(action='ignore')
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier

rankList = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "EMERALD", "DIAMOND", "MASTER", "GRANDMASTER", "CHALLENGER"]
modelNameList = ["CatBoost", "ExtraTree", "LightGBM", "RandomForest"]
colList = ["accuracy_score", "F1_score", "roc_auc_score"]
idxList = [
    ["IRON", "IRON", "IRON", "IRON", 
    "BRONZE", "BRONZE", "BRONZE", "BRONZE", 
    "SILVER", "SILVER", "SILVER", "SILVER", 
    "GOLD", "GOLD", "GOLD", "GOLD", 
    "PLATINUM", "PLATINUM", "PLATINUM", "PLATINUM", 
    "EMERALD", "EMERALD", "EMERALD", "EMERALD", 
    "DIAMOND", "DIAMOND", "DIAMOND", "DIAMOND", 
    "MASTER", "MASTER", "MASTER", "MASTER", 
    "GRANDMASTER", "GRANDMASTER", "GRANDMASTER", "GRANDMASTER", 
    "CHALLENGER", "CHALLENGER", "CHALLENGER", "CHALLENGER"],
    ["CatBoost", "ExtraTree", "LightGBM", "RandomForest",
     "CatBoost", "ExtraTree", "LightGBM", "RandomForest",
     "CatBoost", "ExtraTree", "LightGBM", "RandomForest",
     "CatBoost", "ExtraTree", "LightGBM", "RandomForest",
     "CatBoost", "ExtraTree", "LightGBM", "RandomForest",
     "CatBoost", "ExtraTree", "LightGBM", "RandomForest",
     "CatBoost", "ExtraTree", "LightGBM", "RandomForest",
     "CatBoost", "ExtraTree", "LightGBM", "RandomForest",
     "CatBoost", "ExtraTree", "LightGBM", "RandomForest",
     "CatBoost", "ExtraTree", "LightGBM", "RandomForest"]
    ]
scoreList = np.empty((0,3))

for rank in rankList:
    data = pd.read_csv(f'../Dataset/preProcessed/{rank}.csv')

    # 랜덤 포레스트
    rf = RandomForestClassifier(max_leaf_nodes=200, random_state=10)
    # 라이트지비엠
    lgbm = LGBMClassifier(n_estimators=100, max_depth=12, num_leaves=25, verbosity=0, min_child_samples=30, random_state=10)
    # 캣부스트
    cat = CatBoostClassifier(iterations=200, depth=7, learning_rate=0.1, l2_leaf_reg=40, verbose=0, random_state=10)
    # 엑스트라트리
    et = ExtraTreesClassifier(max_depth=7, max_features=None, random_state=10)

    x = data[data.columns.difference(['result'])]
    y = data['result']

    modelList = [cat, et, lgbm, rf]
    for i in range(4):
        scores = []
        model = modelList[i]

        x_train, x_test, y_train, y_test = train_test_split(x, y, 
                                                        test_size = 0.2, random_state = 42)
        y_train = y_train.values.ravel()
        model.fit(x_train, y_train)
        pre_test = model.predict(x_test)
        pre_train = model.predict(x_train)
        if model == cat:
            printModel = f"CatBoost{model.get_params()}"
        else:
            printModel = model
        
        scores.append(str(round(accuracy_score(y_test, pre_test)*100, 2)) + "%")
        scores.append(str(round(f1_score(y_test, pre_test)*100, 2)) + "%")
        scores.append(str(round(roc_auc_score(y_test, pre_test)*100, 2)) + "%")
        scoreList = np.append(scoreList, np.array([scores]), axis=0)

output = pd.DataFrame(scoreList, columns=colList, index=idxList)
print(output)