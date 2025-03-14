import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Grandmaster = pd.read_csv('Dataset/perMinuteDataset/10min/Grandmaster.csv')

win_Grandmaster = Grandmaster[['Diff_FirstBLOOD', 'Diff_FirstDRAGON',
       'Diff_FirstHERALD', 'Diff_Firsttower', 'dragonType', 'WIN_invadeKill', 'WIN_invadeDeath','WIN_controlWARDPlaced', 
       'WIN_Kill_top', 'WIN_Kill_jgl', 'WIN_Kill_mid', 'WIN_Kill_ad', 'WIN_Kill_sup',
       'WIN_Death_top', 'WIN_Death_jgl', 'WIN_Death_mid', 'WIN_Death_ad', 'WIN_Death_sup', 
       'WIN_Asisst_top', 'WIN_Asisst_jgl', 'WIN_Asisst_mid', 'WIN_Asisst_ad', 'WIN_Asisst_sup',
       'WIN_LV_top', 'WIN_LV_jgl', 'WIN_LV_mid', 'WIN_LV_ad', 'WIN_LV_sup',
       'WIN_CS_top', 'WIN_CS_jgl', 'WIN_CS_mid', 'WIN_CS_ad', 'WIN_CS_sup',
       'WIN_jglCS_top', 'WIN_jglCS_jgl', 'WIN_jglCS_mid', 'WIN_jglCS_ad', 'WIN_jglCS_sup',
       'WIN_GOLD_top', 'WIN_GOLD_jgl', 'WIN_GOLD_mid', 'WIN_GOLD_ad', 'WIN_GOLD_sup',
       'WIN_WARDkill', 'WIN_Inhibitor','WIN_TOWERkill', 'WIN_WARDplaced']]
lose_Grandmaster = Grandmaster[['Diff_FirstBLOOD', 'Diff_FirstDRAGON',
       'Diff_FirstHERALD', 'Diff_Firsttower', 'dragonType',
       'LOSE_invadeDeath', 'LOSE_invadeKill',
       'LOSE_controlWARDPlaced',
       'LOSE_Kill_top', 'LOSE_Kill_jgl', 'LOSE_Kill_mid', 'LOSE_Kill_ad', 'LOSE_Kill_sup',
       'LOSE_Death_top', 'LOSE_Death_jgl',
       'LOSE_Death_mid', 'LOSE_Death_ad', 'LOSE_Death_sup',
       'LOSE_Asisst_top', 'LOSE_Asisst_jgl', 'LOSE_Asisst_mid',
       'LOSE_Asisst_ad', 'LOSE_Asisst_sup',
       'LOSE_LV_top', 'LOSE_LV_jgl',
       'LOSE_LV_mid', 'LOSE_LV_ad', 'LOSE_LV_sup',
       'LOSE_CS_top', 'LOSE_CS_jgl',
       'LOSE_CS_mid', 'LOSE_CS_ad', 'LOSE_CS_sup',
       'LOSE_jglCS_top', 'LOSE_jglCS_jgl', 'LOSE_jglCS_mid', 'LOSE_jglCS_ad', 'LOSE_jglCS_sup',
       'LOSE_GOLD_top', 'LOSE_GOLD_jgl',
       'LOSE_GOLD_mid', 'LOSE_GOLD_ad', 'LOSE_GOLD_sup',
       'LOSE_WARDkill', 'LOSE_Inhibitor',
       'LOSE_TOWERkill', 'LOSE_WARDplaced']]
colName = 'WIN'
win_Grandmaster = win_Grandmaster.rename(columns={f'{colName}_invadeKill': 'invadeKill', f'{colName}_invadeDeath': 'invadeDeath', 
                                                  f'{colName}_controlWARDPlaced': 'controlWARDPlaced',
                                                  f'{colName}_Kill_top': 'Kill_top',f'{colName}_Kill_jgl': 'Kill_jgl',f'{colName}_Kill_mid': 'Kill_mid',f'{colName}_Kill_ad': 'Kill_ad', f'{colName}_Kill_sup': 'Kill_sup',
                                                  f'{colName}_Death_top': 'Death_top',f'{colName}_Death_jgl': 'Death_jgl',f'{colName}_Death_mid': 'Death_mid',f'{colName}_Death_ad': 'Death_ad',f'{colName}_Death_sup': 'Death_sup',
                                                  f'{colName}_Asisst_top': 'Assist_top',f'{colName}_Asisst_jgl': 'Assist_jgl',f'{colName}_Asisst_mid': 'Assist_mid',f'{colName}_Asisst_ad': 'Assist_ad',f'{colName}_Asisst_sup': 'Assist_sup',
                                                  f'{colName}_LV_top': 'LV_top',f'{colName}_LV_jgl': 'LV_jgl',f'{colName}_LV_mid': 'LV_mid',f'{colName}_LV_ad': 'LV_ad',f'{colName}_LV_sup': 'LV_sup',
                                                  f'{colName}_CS_top': 'CS_top',f'{colName}_CS_jgl': 'CS_jgl',f'{colName}_CS_mid': 'CS_mid',f'{colName}_CS_ad': 'CS_ad',f'{colName}_CS_sup': 'CS_sup',
                                                  f'{colName}_jglCS_top': 'jglCS_top',f'{colName}_jglCS_jgl': 'jglCS_jgl',f'{colName}_jglCS_mid': 'jglCS_mid',f'{colName}_jglCS_ad': 'jglCS_ad',f'{colName}_jglCS_sup': 'jglCS_sup',
                                                  f'{colName}_GOLD_top': 'GOLD_top',f'{colName}_GOLD_jgl': 'GOLD_jgl',f'{colName}_GOLD_mid': 'GOLD_mid',f'{colName}_GOLD_ad': 'GOLD_ad',f'{colName}_GOLD_sup': 'GOLD_sup',
                                                  f'{colName}_WARDkill': 'WARDkill',f'{colName}_Inhibitor': 'Inhibitor',f'{colName}_TOWERkill': 'TOWERkill',f'{colName}_WARDplaced': 'WARDplaced'})

colName = 'LOSE'
lose_Grandmaster = lose_Grandmaster.rename(columns={f'{colName}_invadeKill': 'invadeKill', f'{colName}_invadeDeath': 'invadeDeath', 
                                                  f'{colName}_controlWARDPlaced': 'controlWARDPlaced',
                                                  f'{colName}_Kill_top': 'Kill_top',f'{colName}_Kill_jgl': 'Kill_jgl',f'{colName}_Kill_mid': 'Kill_mid',f'{colName}_Kill_ad': 'Kill_ad', f'{colName}_Kill_sup': 'Kill_sup',
                                                  f'{colName}_Death_top': 'Death_top',f'{colName}_Death_jgl': 'Death_jgl',f'{colName}_Death_mid': 'Death_mid',f'{colName}_Death_ad': 'Death_ad',f'{colName}_Death_sup': 'Death_sup',
                                                  f'{colName}_Asisst_top': 'Assist_top',f'{colName}_Asisst_jgl': 'Assist_jgl',f'{colName}_Asisst_mid': 'Assist_mid',f'{colName}_Asisst_ad': 'Assist_ad',f'{colName}_Asisst_sup': 'Assist_sup',
                                                  f'{colName}_LV_top': 'LV_top',f'{colName}_LV_jgl': 'LV_jgl',f'{colName}_LV_mid': 'LV_mid',f'{colName}_LV_ad': 'LV_ad',f'{colName}_LV_sup': 'LV_sup',
                                                  f'{colName}_CS_top': 'CS_top',f'{colName}_CS_jgl': 'CS_jgl',f'{colName}_CS_mid': 'CS_mid',f'{colName}_CS_ad': 'CS_ad',f'{colName}_CS_sup': 'CS_sup',
                                                  f'{colName}_jglCS_top': 'jglCS_top',f'{colName}_jglCS_jgl': 'jglCS_jgl',f'{colName}_jglCS_mid': 'jglCS_mid',f'{colName}_jglCS_ad': 'jglCS_ad',f'{colName}_jglCS_sup': 'jglCS_sup',
                                                  f'{colName}_GOLD_top': 'GOLD_top',f'{colName}_GOLD_jgl': 'GOLD_jgl',f'{colName}_GOLD_mid': 'GOLD_mid',f'{colName}_GOLD_ad': 'GOLD_ad',f'{colName}_GOLD_sup': 'GOLD_sup',
                                                  f'{colName}_WARDkill': 'WARDkill',f'{colName}_Inhibitor': 'Inhibitor',f'{colName}_TOWERkill': 'TOWERkill',f'{colName}_WARDplaced': 'WARDplaced'})
win_Grandmaster['result'] = 1
lose_Grandmaster['result'] = -1
df = pd.concat([win_Grandmaster, lose_Grandmaster], axis=0, ignore_index=True)

columns = np.array(df.columns)
df_small = df[columns]
df_corr = df_small.corr()
plt.figure(figsize=(5, 5))
sns.heatmap(df_corr, annot=True, fmt=".2f", cmap="Blues")

plt.show()