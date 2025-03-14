import pandas as pd
import matplotlib.pyplot as plt
import numpy as np





#가져올 데이터셋 선택
data = pd.read_csv(f'Dataset/perMinuteDataset/10min/GRANDMASTER.csv')
#data2 = pd.read_csv('Dataset/lose/Gold_I_lose.csv')
#data = pd.concat([data1], ignore_index=True)

global win_df, lose_df

win_df = data[['Diff_FirstBLOOD', 'Diff_FirstDRAGON', 'dragonType', 'WIN_controlWARDPlaced', 
       'WIN_Kill_top', 'WIN_Kill_jgl', 'WIN_Kill_mid', 'WIN_Kill_ad', 'WIN_Kill_sup',
       # 'WIN_Death_top', 'WIN_Death_jgl', 'WIN_Death_mid', 'WIN_Death_ad', 'WIN_Death_sup', 
       'WIN_Asisst_top', 'WIN_Asisst_jgl', 'WIN_Asisst_mid', 'WIN_Asisst_ad', 'WIN_Asisst_sup',
       'WIN_LV_top', 'WIN_LV_jgl', 'WIN_LV_mid', 'WIN_LV_ad', 'WIN_LV_sup',
       'WIN_CS_top', 'WIN_CS_jgl', 'WIN_CS_mid', 'WIN_CS_ad', 'WIN_CS_sup',
       'WIN_jglCS_top', 'WIN_jglCS_jgl', 'WIN_jglCS_mid', 'WIN_jglCS_ad', 'WIN_jglCS_sup',
       # 'WIN_GOLD_top', 'WIN_GOLD_jgl', 'WIN_GOLD_mid', 'WIN_GOLD_ad', 'WIN_GOLD_sup',
       'WIN_WARDkill']]
lose_df = data[['Diff_FirstBLOOD', 'Diff_FirstDRAGON', 'dragonType',
       'LOSE_controlWARDPlaced',
       'LOSE_Kill_top', 'LOSE_Kill_jgl', 'LOSE_Kill_mid', 'LOSE_Kill_ad', 'LOSE_Kill_sup',
       # 'LOSE_Death_top', 'LOSE_Death_jgl', 'LOSE_Death_mid', 'LOSE_Death_ad', 'LOSE_Death_sup',
       'LOSE_Asisst_top', 'LOSE_Asisst_jgl', 'LOSE_Asisst_mid', 'LOSE_Asisst_ad', 'LOSE_Asisst_sup',
       'LOSE_LV_top', 'LOSE_LV_jgl', 'LOSE_LV_mid', 'LOSE_LV_ad', 'LOSE_LV_sup',
       'LOSE_CS_top', 'LOSE_CS_jgl', 'LOSE_CS_mid', 'LOSE_CS_ad', 'LOSE_CS_sup',
       'LOSE_jglCS_top', 'LOSE_jglCS_jgl', 'LOSE_jglCS_mid', 'LOSE_jglCS_ad', 'LOSE_jglCS_sup',
       # 'LOSE_GOLD_top', 'LOSE_GOLD_jgl', 'LOSE_GOLD_mid', 'LOSE_GOLD_ad', 'LOSE_GOLD_sup',
       'LOSE_WARDkill']]
colName = 'WIN'
win_df = win_df.rename(columns={f'{colName}_controlWARDPlaced': 'controlWARDPlaced',
                                                  f'{colName}_Kill_top': 'Kill_top',f'{colName}_Kill_jgl': 'Kill_jgl',f'{colName}_Kill_mid': 'Kill_mid',f'{colName}_Kill_ad': 'Kill_ad', f'{colName}_Kill_sup': 'Kill_sup',
                                                 #  f'{colName}_Death_top': 'Death_top',f'{colName}_Death_jgl': 'Death_jgl',f'{colName}_Death_mid': 'Death_mid',f'{colName}_Death_ad': 'Death_ad',f'{colName}_Death_sup': 'Death_sup',
                                                  f'{colName}_Asisst_top': 'Asisst_top',f'{colName}_Asisst_jgl': 'Asisst_jgl',f'{colName}_Asisst_mid': 'Asisst_mid',f'{colName}_Asisst_ad': 'Asisst_ad',f'{colName}_Asisst_sup': 'Asisst_sup',
                                                  f'{colName}_LV_top': 'LV_top',f'{colName}_LV_jgl': 'LV_jgl',f'{colName}_LV_mid': 'LV_mid',f'{colName}_LV_ad': 'LV_ad',f'{colName}_LV_sup': 'LV_sup',
                                                  f'{colName}_CS_top': 'CS_top',f'{colName}_CS_jgl': 'CS_jgl',f'{colName}_CS_mid': 'CS_mid',f'{colName}_CS_ad': 'CS_ad',f'{colName}_CS_sup': 'CS_sup',
                                                  f'{colName}_jglCS_top': 'jglCS_top',f'{colName}_jglCS_jgl': 'jglCS_jgl',f'{colName}_jglCS_mid': 'jglCS_mid',f'{colName}_jglCS_ad': 'jglCS_ad',f'{colName}_jglCS_sup': 'jglCS_sup',
                                                 #  f'{colName}_GOLD_top': 'GOLD_top',f'{colName}_GOLD_jgl': 'GOLD_jgl',f'{colName}_GOLD_mid': 'GOLD_mid',f'{colName}_GOLD_ad': 'GOLD_ad',f'{colName}_GOLD_sup': 'GOLD_sup',
                                                  f'{colName}_WARDkill': 'WARDkill'})

colName = 'LOSE'
lose_df = lose_df.rename(columns={f'{colName}_controlWARDPlaced': 'controlWARDPlaced',
                                                  f'{colName}_Kill_top': 'Kill_top',f'{colName}_Kill_jgl': 'Kill_jgl',f'{colName}_Kill_mid': 'Kill_mid',f'{colName}_Kill_ad': 'Kill_ad', f'{colName}_Kill_sup': 'Kill_sup',
                                                 #  f'{colName}_Death_top': 'Death_top',f'{colName}_Death_jgl': 'Death_jgl',f'{colName}_Death_mid': 'Death_mid',f'{colName}_Death_ad': 'Death_ad',f'{colName}_Death_sup': 'Death_sup',
                                                  f'{colName}_Asisst_top': 'Asisst_top',f'{colName}_Asisst_jgl': 'Asisst_jgl',f'{colName}_Asisst_mid': 'Asisst_mid',f'{colName}_Asisst_ad': 'Asisst_ad',f'{colName}_Asisst_sup': 'Asisst_sup',
                                                  f'{colName}_LV_top': 'LV_top',f'{colName}_LV_jgl': 'LV_jgl',f'{colName}_LV_mid': 'LV_mid',f'{colName}_LV_ad': 'LV_ad',f'{colName}_LV_sup': 'LV_sup',
                                                  f'{colName}_CS_top': 'CS_top',f'{colName}_CS_jgl': 'CS_jgl',f'{colName}_CS_mid': 'CS_mid',f'{colName}_CS_ad': 'CS_ad',f'{colName}_CS_sup': 'CS_sup',
                                                  f'{colName}_jglCS_top': 'jglCS_top',f'{colName}_jglCS_jgl': 'jglCS_jgl',f'{colName}_jglCS_mid': 'jglCS_mid',f'{colName}_jglCS_ad': 'jglCS_ad',f'{colName}_jglCS_sup': 'jglCS_sup',
                                                 #  f'{colName}_GOLD_top': 'GOLD_top',f'{colName}_GOLD_jgl': 'GOLD_jgl',f'{colName}_GOLD_mid': 'GOLD_mid',f'{colName}_GOLD_ad': 'GOLD_ad',f'{colName}_GOLD_sup': 'GOLD_sup',
                                                  f'{colName}_WARDkill': 'WARDkill'})


def mergeCol(colName):
    global win_df, lose_df
    win_df[colName] = (win_df[f'{colName}_ad']+win_df[f'{colName}_top']+win_df[f'{colName}_jgl']+win_df[f'{colName}_mid']+win_df[f'{colName}_sup'])
    lose_df[colName] = (lose_df[f'{colName}_ad']+lose_df[f'{colName}_top']+lose_df[f'{colName}_jgl']+lose_df[f'{colName}_mid']+lose_df[f'{colName}_sup'])
    win_df= win_df.drop([f'{colName}_ad', f'{colName}_top', f'{colName}_jgl', f'{colName}_mid', f'{colName}_sup'],axis=1)
    lose_df= lose_df.drop([f'{colName}_ad', f'{colName}_top', f'{colName}_jgl', f'{colName}_mid', f'{colName}_sup'],axis=1)
    return win_df, lose_df

win_df, lose_df = mergeCol('Kill')
# win_df, lose_df = mergeCol('Death')
win_df, lose_df = mergeCol('Asisst')
win_df, lose_df = mergeCol('LV')
win_df, lose_df = mergeCol('CS')
win_df, lose_df = mergeCol('jglCS')
# win_df, lose_df = mergeCol('GOLD')

win_df['Kill'] = win_df['Kill'] - lose_df['Kill'] 
lose_df['Kill'] = win_df['Kill']*-1
# win_df['Death'] = win_df['Death'] - lose_df['Death'] 
# lose_df['Death'] = win_df['Death']*-1
win_df['LV'] = win_df['LV']-lose_df['LV']
lose_df['LV'] = win_df['LV']*-1
win_df['CS'] = win_df['CS'] - lose_df['CS'] 
lose_df['CS'] = win_df['CS']*-1
win_df['jglCS'] = win_df['jglCS'] - lose_df['jglCS'] 
lose_df['jglCS'] = win_df['jglCS']*-1
# win_df['GOLD'] = win_df['GOLD'] - lose_df['GOLD'] 
# lose_df['GOLD'] = win_df['GOLD']*-1

# win_df.head()



# 한 그래프에 박스플롯으로 그리기
# plt.figure(figsize=(12, 6))

# win_df.boxplot(column=list(win_df.columns), vert=False)
# plt.xlabel("data")
# plt.ylabel("name")

# plt.show()



# 한 그래프에 막대형식(bar chart)으로 그리기
# plt.figure(figsize=(12, 6))

# data[column].mean()=평균막대(색깔)
# yerr=data[column].std()=표준편차(검정)

# for column in win_df.columns:
#     plt.bar(column, win_df[column].mean(),yerr=win_df[column].std(), capsize=5)

# plt.xlabel("column")
# plt.ylabel("data")
# plt.xticks(rotation=90)
# plt.show()



#한 칼럼의 대한 분포도를 자세히 보고싶을때

#칼럼 선택
# plt.hist(win_df['controlWARDPlaced'], align='mid', bins=6)
#plt.xticks(data['dragonType'])

# plt.title('controlWARDPlaced')
# plt.xlabel('data')
# plt.ylabel('Frequency')
# plt.show()


#한 화면에 선택한 그래프를 한눈에 보고 싶을때(막대 그래프)

#2*6 격자로 히스토그램 출력
fig, axes = plt.subplots(nrows=2, ncols=6, figsize=(15, 6))

# 각각의 칼럼에 대한 히스토그램 그리기
for i, column in enumerate(win_df.columns):
    row, col = divmod(i, 6)
    axes[row, col].hist(win_df[column], align='mid', bins=6)
    axes[row, col].set_title(column)
    axes[row, col].set_xlabel('data')
    axes[row, col].set_ylabel('Frequency')

plt.tight_layout()
plt.show()