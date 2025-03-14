import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def mergeCol(win_df, lose_df, colName):
    win_df[colName] = (win_df[f'{colName}_ad']+win_df[f'{colName}_top']+win_df[f'{colName}_jgl']+win_df[f'{colName}_mid']+win_df[f'{colName}_sup'])
    lose_df[colName] = (lose_df[f'{colName}_ad']+lose_df[f'{colName}_top']+lose_df[f'{colName}_jgl']+lose_df[f'{colName}_mid']+lose_df[f'{colName}_sup'])
    win_df= win_df.drop([f'{colName}_ad', f'{colName}_top', f'{colName}_jgl', f'{colName}_mid', f'{colName}_sup'],axis=1)
    lose_df= lose_df.drop([f'{colName}_ad', f'{colName}_top', f'{colName}_jgl', f'{colName}_mid', f'{colName}_sup'],axis=1)
    return win_df, lose_df

def mulMinus1(win_df, lose_df, colName):
    win_df[f'Diff_{colName}'] = win_df[colName]-lose_df[colName]
    lose_df[f'Diff_{colName}'] = win_df[f'Diff_{colName}'] * -1
    win_df = win_df.drop([colName], axis=1)
    lose_df = lose_df.drop([colName], axis=1)
    return win_df, lose_df

df = pd.read_csv(f'../Dataset/perMinuteDataset/10min/CHALLENGER.csv')
win_df = df[['Diff_FirstBLOOD', 'Diff_FirstDRAGON',
    'dragonType', 'WIN_controlWARDPlaced', 'WIN_WARDplaced',
    'WIN_Kill_top', 'WIN_Kill_jgl', 'WIN_Kill_mid', 'WIN_Kill_ad', 'WIN_Kill_sup',
    'WIN_Death_top', 'WIN_Death_jgl', 'WIN_Death_mid', 'WIN_Death_ad', 'WIN_Death_sup', 
    'WIN_Asisst_top', 'WIN_Asisst_jgl', 'WIN_Asisst_mid', 'WIN_Asisst_ad', 'WIN_Asisst_sup',
    'WIN_LV_top', 'WIN_LV_jgl', 'WIN_LV_mid', 'WIN_LV_ad', 'WIN_LV_sup',
    'WIN_CS_top', 'WIN_CS_jgl', 'WIN_CS_mid', 'WIN_CS_ad', 'WIN_CS_sup',
    'WIN_jglCS_top', 'WIN_jglCS_jgl', 'WIN_jglCS_mid', 'WIN_jglCS_ad', 'WIN_jglCS_sup',
    'WIN_WARDkill']]
lose_df = df[['Diff_FirstBLOOD', 'Diff_FirstDRAGON',
    'dragonType', 'LOSE_controlWARDPlaced', 'LOSE_WARDplaced',
    'LOSE_Kill_top', 'LOSE_Kill_jgl', 'LOSE_Kill_mid', 'LOSE_Kill_ad', 'LOSE_Kill_sup',
    'LOSE_Death_top', 'LOSE_Death_jgl', 'LOSE_Death_mid', 'LOSE_Death_ad', 'LOSE_Death_sup',
    'LOSE_Asisst_top', 'LOSE_Asisst_jgl', 'LOSE_Asisst_mid', 'LOSE_Asisst_ad', 'LOSE_Asisst_sup',
    'LOSE_LV_top', 'LOSE_LV_jgl', 'LOSE_LV_mid', 'LOSE_LV_ad', 'LOSE_LV_sup',
    'LOSE_CS_top', 'LOSE_CS_jgl', 'LOSE_CS_mid', 'LOSE_CS_ad', 'LOSE_CS_sup',
    'LOSE_jglCS_top', 'LOSE_jglCS_jgl', 'LOSE_jglCS_mid', 'LOSE_jglCS_ad', 'LOSE_jglCS_sup',
    'LOSE_WARDkill']]

colName = 'WIN'
win_df = win_df.rename(columns={f'{colName}_controlWARDPlaced': 'controlWARDPlaced', 
                                # f'{colName}_Firsttower': 'Firsttower',
                                                f'{colName}_Kill_top': 'Kill_top',f'{colName}_Kill_jgl': 'Kill_jgl',f'{colName}_Kill_mid': 'Kill_mid',f'{colName}_Kill_ad': 'Kill_ad', f'{colName}_Kill_sup': 'Kill_sup',
                                                f'{colName}_Death_top': 'Death_top',f'{colName}_Death_jgl': 'Death_jgl',f'{colName}_Death_mid': 'Death_mid',f'{colName}_Death_ad': 'Death_ad',f'{colName}_Death_sup': 'Death_sup',
                                                f'{colName}_Asisst_top': 'Asisst_top',f'{colName}_Asisst_jgl': 'Asisst_jgl',f'{colName}_Asisst_mid': 'Asisst_mid',f'{colName}_Asisst_ad': 'Asisst_ad',f'{colName}_Asisst_sup': 'Asisst_sup',
                                                f'{colName}_LV_top': 'LV_top',f'{colName}_LV_jgl': 'LV_jgl',f'{colName}_LV_mid': 'LV_mid',f'{colName}_LV_ad': 'LV_ad',f'{colName}_LV_sup': 'LV_sup',
                                                f'{colName}_CS_top': 'CS_top',f'{colName}_CS_jgl': 'CS_jgl',f'{colName}_CS_mid': 'CS_mid',f'{colName}_CS_ad': 'CS_ad',f'{colName}_CS_sup': 'CS_sup',
                                                f'{colName}_jglCS_top': 'jglCS_top',f'{colName}_jglCS_jgl': 'jglCS_jgl',f'{colName}_jglCS_mid': 'jglCS_mid',f'{colName}_jglCS_ad': 'jglCS_ad',f'{colName}_jglCS_sup': 'jglCS_sup',
                                                f'{colName}_WARDplaced': 'WARDplaced', f'{colName}_WARDkill': 'WARDkill'})

colName = 'LOSE'
lose_df = lose_df.rename(columns={f'{colName}_controlWARDPlaced': 'controlWARDPlaced',
                                                f'{colName}_Kill_top': 'Kill_top',f'{colName}_Kill_jgl': 'Kill_jgl',f'{colName}_Kill_mid': 'Kill_mid',f'{colName}_Kill_ad': 'Kill_ad', f'{colName}_Kill_sup': 'Kill_sup',
                                                f'{colName}_Death_top': 'Death_top',f'{colName}_Death_jgl': 'Death_jgl',f'{colName}_Death_mid': 'Death_mid',f'{colName}_Death_ad': 'Death_ad',f'{colName}_Death_sup': 'Death_sup',
                                                f'{colName}_Asisst_top': 'Asisst_top',f'{colName}_Asisst_jgl': 'Asisst_jgl',f'{colName}_Asisst_mid': 'Asisst_mid',f'{colName}_Asisst_ad': 'Asisst_ad',f'{colName}_Asisst_sup': 'Asisst_sup',
                                                f'{colName}_LV_top': 'LV_top',f'{colName}_LV_jgl': 'LV_jgl',f'{colName}_LV_mid': 'LV_mid',f'{colName}_LV_ad': 'LV_ad',f'{colName}_LV_sup': 'LV_sup',
                                                f'{colName}_CS_top': 'CS_top',f'{colName}_CS_jgl': 'CS_jgl',f'{colName}_CS_mid': 'CS_mid',f'{colName}_CS_ad': 'CS_ad',f'{colName}_CS_sup': 'CS_sup',
                                                f'{colName}_jglCS_top': 'jglCS_top',f'{colName}_jglCS_jgl': 'jglCS_jgl',f'{colName}_jglCS_mid': 'jglCS_mid',f'{colName}_jglCS_ad': 'jglCS_ad',f'{colName}_jglCS_sup': 'jglCS_sup',
                                                f'{colName}_WARDplaced': 'WARDplaced', f'{colName}_WARDkill': 'WARDkill'})

win_df, lose_df = mergeCol(win_df, lose_df, 'Kill')
win_df, lose_df = mergeCol(win_df, lose_df, 'Asisst')
win_df, lose_df = mergeCol(win_df, lose_df, 'LV')
win_df, lose_df = mergeCol(win_df, lose_df, 'CS')
win_df, lose_df = mergeCol(win_df, lose_df, 'Death')
win_df, lose_df = mergeCol(win_df, lose_df, 'jglCS')    

win_df, lose_df = mulMinus1(win_df, lose_df, 'Kill')
win_df, lose_df = mulMinus1(win_df, lose_df, 'Asisst')
win_df, lose_df = mulMinus1(win_df, lose_df, 'LV')
win_df, lose_df = mulMinus1(win_df, lose_df, 'CS')
win_df, lose_df = mulMinus1(win_df, lose_df, 'Death')
win_df, lose_df = mulMinus1(win_df, lose_df, 'WARDplaced')
win_df, lose_df = mulMinus1(win_df, lose_df, 'WARDkill')
win_df, lose_df = mulMinus1(win_df, lose_df, 'controlWARDPlaced')
win_df, lose_df = mulMinus1(win_df, lose_df, 'jglCS')

lose_df['Diff_FirstBLOOD'] = win_df['Diff_FirstBLOOD']*-1
lose_df['Diff_FirstDRAGON'] = win_df['Diff_FirstDRAGON']*-1

win_df['FirstDragon_AIR_DRAGON'] = np.where((win_df['Diff_FirstDRAGON'] == 1) & (win_df['dragonType'] == 1), 1, 0)
win_df['FirstDragon_EARTH_DRAGON'] = np.where((win_df['Diff_FirstDRAGON'] == 1) & (win_df['dragonType'] == 2), 1, 0)
win_df['FirstDragon_FIRE_DRAGON'] = np.where((win_df['Diff_FirstDRAGON'] == 1) & (win_df['dragonType'] == 3), 1, 0)
win_df['FirstDragon_WATER_DRAGON'] = np.where((win_df['Diff_FirstDRAGON'] == 1) & (win_df['dragonType'] == 4), 1, 0)
win_df['FirstDragon_HEXTECH_DRAGON'] = np.where((win_df['Diff_FirstDRAGON'] == 1) & (win_df['dragonType'] == 5), 1, 0)
win_df['FirstDragon_CHEMTECH_DRAGON'] = np.where((win_df['Diff_FirstDRAGON'] == 1) & (win_df['dragonType'] == 6), 1, 0)
lose_df['FirstDragon_AIR_DRAGON'] = np.where((lose_df['Diff_FirstDRAGON'] == 1) & (lose_df['dragonType'] == 1), 1, 0)
lose_df['FirstDragon_EARTH_DRAGON'] = np.where((lose_df['Diff_FirstDRAGON'] == 1) & (lose_df['dragonType'] == 2), 1, 0)
lose_df['FirstDragon_FIRE_DRAGON'] = np.where((lose_df['Diff_FirstDRAGON'] == 1) & (lose_df['dragonType'] == 3), 1, 0)
lose_df['FirstDragon_WATER_DRAGON'] = np.where((lose_df['Diff_FirstDRAGON'] == 1) & (lose_df['dragonType'] == 4), 1, 0)
lose_df['FirstDragon_HEXTECH_DRAGON'] = np.where((lose_df['Diff_FirstDRAGON'] == 1) & (lose_df['dragonType'] == 5), 1, 0)
lose_df['FirstDragon_CHEMTECH_DRAGON'] = np.where((lose_df['Diff_FirstDRAGON'] == 1) & (lose_df['dragonType'] == 6), 1, 0)
win_df['result'] = 1
lose_df['result'] = 0
df = pd.concat([win_df, lose_df], axis=0)
df = df.drop(['dragonType'], axis=1)
columns = np.array(df.columns)
# print(columns)
df_small = df[columns]
# print(df_small)
df_corr = df_small.corr()
print(df.corr()['result'])
# print(df_corr)
plt.figure(figsize=(10,10))
sns.heatmap(df_corr, annot=True, cmap="Blues")

plt.show()