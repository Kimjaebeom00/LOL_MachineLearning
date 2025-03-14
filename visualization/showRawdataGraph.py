import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



#가져올 데이터셋 선택
data1 = pd.read_csv('Dataset/win/Gold_I.csv')
data2 = pd.read_csv('Dataset/lose/Gold_I_lose.csv')
data = pd.concat([data1, data2], ignore_index=True)
#버리는 데이터
data= data.drop(['matchId'],axis=1)
data= data.drop(['queueId'],axis=1)
data= data.drop(['result'],axis=1)
data= data.drop(['Diff_WARDplaced'],axis=1)
data= data.drop(['K-WIN-top'],axis=1)
data= data.drop(['K-LOSE-top'],axis=1)
data= data.drop(['K-WIN-jug'],axis=1)
data= data.drop(['K-LOSE-jug'],axis=1)
data= data.drop(['K-WIN-mid'],axis=1)
data= data.drop(['K-LOSE-mid'],axis=1)
data= data.drop(['K-WIN-ad'],axis=1)
data= data.drop(['K-LOSE-ad'],axis=1)
data= data.drop(['K-WIN-sup'],axis=1)
data= data.drop(['K-LOSE-sup'],axis=1)
data= data.drop(['LOSE_controlWARDPlaced'],axis=1)
data= data.drop(['WIN_controlWARDPlaced'],axis=1)

# 한 그래프에 박스플롯으로 그리기
# plt.figure(figsize=(12, 6))

# data.boxplot(column=list(data.columns), vert=False)
# plt.xlabel("data")
# plt.ylabel("name")

# plt.show()


# 한 그래프에 막대형식(bar chart)으로 그리기
# plt.figure(figsize=(12, 6))

#data[column].mean()=평균막대(색깔)
#yerr=data[column].std()=표준편차(검정)
for column in data.columns:
    plt.bar(column, data[column].mean(),yerr=data[column].std(), capsize=5)

plt.xlabel("column")
plt.ylabel("data")
plt.xticks(rotation=90)
plt.show()


#한 칼럼의 대한 분포도를 자세히 보고싶을때

#칼럼 선택
# plt.hist(data['Diff_CS'], bins=20)

# plt.xlabel('data')
# plt.ylabel('Frequency')
# plt.show()