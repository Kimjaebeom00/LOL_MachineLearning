from getData import getDataset
import csv
import time
from getData import getLoseDataset
import pandas as pd



def save_dataframe_to_csv(dataframe, filename):
    df = pd.DataFrame(dataframe)
    columns_to_exclude_index = [0, 1, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 26, 34]  
    columns_to_multiply_by_minus_1_index = [col_idx for col_idx in range(len(df.columns)) if col_idx not in columns_to_exclude_index]
    df.iloc[:, columns_to_multiply_by_minus_1_index] = df.iloc[:, columns_to_multiply_by_minus_1_index] * -1
    df.to_csv(filename, index=False)


fieldnames = [
        'matchId',
        'queueId',
        'Diff_LV',
        'Diff_CS',
        'Diff_jglCS',
        'Diff-K',
        'Diff-K-top',
        'K-WIN-top',
        'K-LOSE-top',
        'Diff-K-jug',
        'K-WIN-jug',
        'K-LOSE-jug',
        'Diff-K-mid',
        'K-WIN-mid',
        'K-LOSE-mid',
        'Diff-K-ad',
        'K-WIN-ad',
        'K-LOSE-ad',
        'Diff-K-sup',
        'K-WIN-sup',
        'K-LOSE-sup',
        'invadeKill',
        'Diff-A',
        'Diff_WARDplaced',
        'Diff-ControlWARDplaced',
        'LOSE_controlWARDPlaced',
        'WIN_controlWARDPlaced',
        'Diff_WARDkill',
        'Diff_Inhibitor',
        'Diff_TOWERkill',
        'Diff_FirstDRAGON',
        'Diff_FirstHERALD',
        'Diff_Firsttower',
        'Diff_FirstBLOOD',
        'dragonType',
        'result'
    ]
def saveDataSetToCSV(matchIdSet, fileName, frame):
    with open(fileName, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        i = 0
        for matchId in matchIdSet:
            i += 1
            try:
                if i%2 == 0:
                    dic_data = getLoseDataset.getResult(matchId, frame, 1)
                else:
                    dic_data = getLoseDataset.getResult(matchId, frame, 2)
            except KeyError:
                print("KeyError발생.. 20초 대기 후 재시도.. ")
                time.sleep(20)
                try:
                    if i%2 == 0:
                        dic_data = getLoseDataset.getResult(matchId, frame, 1)
                    else:
                        dic_data = getLoseDataset.getResult(matchId, frame, 2)
                except KeyError:
                    continue
            if dic_data == 0:
                time.sleep(1.2)
                continue
            w.writerow(dic_data)
            print(f'{i} : {matchId}의 데이터 추가')
            time.sleep(1.2)

# 데이터 수집하다가 중간에 끊겼을 때 사용 (th에 최종 출력된 인덱스 번호 넣으면 됨)
def append_saveDataSetToCSV(matchIdSet, fileName, frame, th):
    with open(fileName, 'a', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        i = th
        for matchId in matchIdSet:
            i += 1
            try:
                if i%2 == 0:
                    dic_data = getLoseDataset.getResult(matchId, frame, 1)
                else:
                    dic_data = getLoseDataset.getResult(matchId, frame, 2)
            except KeyError:
                print("KeyError발생.. 20초 대기 후 재시도.. ")
                time.sleep(20)
                try:
                    if i%2 == 0:
                        dic_data = getLoseDataset.getResult(matchId, frame, 1)
                    else:
                        dic_data = getLoseDataset.getResult(matchId, frame, 2)
                except KeyError:
                    continue
            if dic_data == 0:
                time.sleep(1.2)
                continue
            w.writerow(dic_data)
            print(f'{i} : {matchId}의 데이터 추가')
            time.sleep(1.2)
