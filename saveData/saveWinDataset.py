from getData import getPerMinDataset
import csv
import time

fieldnames = [
    'queueId', 'matchId', 
    'Diff_FirstBLOOD', 'Diff_FirstDRAGON', 'Diff_FirstHERALD', 'Diff_Firsttower', 'dragonType', 
    'WIN_invadeKill', 'LOSE_invadeDeath', 'LOSE_invadeKill', 'WIN_invadeDeath', 
    'WIN_controlWARDPlaced', 'LOSE_controlWARDPlaced', 
    'WIN_Kill_top', 'WIN_Kill_jgl', 'WIN_Kill_mid', 'WIN_Kill_ad', 'WIN_Kill_sup', 
    'LOSE_Kill_top', 'LOSE_Kill_jgl', 'LOSE_Kill_mid', 'LOSE_Kill_ad', 'LOSE_Kill_sup', 
    'WIN_Death_top', 'WIN_Death_jgl', 'WIN_Death_mid', 'WIN_Death_ad', 'WIN_Death_sup',
    'LOSE_Death_top', 'LOSE_Death_jgl', 'LOSE_Death_mid', 'LOSE_Death_ad', 'LOSE_Death_sup',
    'WIN_Asisst_top', 'WIN_Asisst_jgl', 'WIN_Asisst_mid', 'WIN_Asisst_ad', 'WIN_Asisst_sup', 
    'LOSE_Asisst_top', 'LOSE_Asisst_jgl', 'LOSE_Asisst_mid', 'LOSE_Asisst_ad', 'LOSE_Asisst_sup', 
    'WIN_LV_top', 'WIN_LV_jgl', 'WIN_LV_mid', 'WIN_LV_ad', 'WIN_LV_sup', 
    'LOSE_LV_top', 'LOSE_LV_jgl', 'LOSE_LV_mid', 'LOSE_LV_ad', 'LOSE_LV_sup',
    'WIN_CS_top', 'WIN_CS_jgl', 'WIN_CS_mid', 'WIN_CS_ad', 'WIN_CS_sup',
    'LOSE_CS_top', 'LOSE_CS_jgl', 'LOSE_CS_mid', 'LOSE_CS_ad', 'LOSE_CS_sup',
    'WIN_jglCS_top', 'WIN_jglCS_jgl', 'WIN_jglCS_mid', 'WIN_jglCS_ad', 'WIN_jglCS_sup',
    'LOSE_jglCS_top', 'LOSE_jglCS_jgl', 'LOSE_jglCS_mid', 'LOSE_jglCS_ad', 'LOSE_jglCS_sup',
    'WIN_GOLD_top', 'WIN_GOLD_jgl', 'WIN_GOLD_mid', 'WIN_GOLD_ad', 'WIN_GOLD_sup', 
    'LOSE_GOLD_top', 'LOSE_GOLD_jgl', 'LOSE_GOLD_mid', 'LOSE_GOLD_ad', 'LOSE_GOLD_sup',   
    'WIN_WARDkill', 'LOSE_WARDkill', 
    'WIN_Inhibitor', 'LOSE_Inhibitor', 
    'WIN_TOWERkill', 'LOSE_TOWERkill',
    'WIN_WARDplaced', 'LOSE_WARDplaced'
    ]
def     saveDataSetToCSV(matchIdSet, frame, tier, idx):
    i = 0
    for matchId in matchIdSet:
        i += 1
        try:
            if i%2 == 0:
                dic_data = getPerMinDataset.getResult(matchId, frame, 1, tier, idx)
            else:
                dic_data = getPerMinDataset.getResult(matchId, frame, 2, tier, idx)
        except KeyError:
            print("KeyError발생.. 20초 대기 후 재시도.. ")
            time.sleep(20)
            try:
                if i%2 == 0:
                    dic_data = getPerMinDataset.getResult(matchId, frame, 1, tier, idx)
                else:
                    dic_data = getPerMinDataset.getResult(matchId, frame, 2, tier, idx)
            except KeyError:
                continue
        idx += 1
        if dic_data == 0:
            time.sleep(1.2)
            continue
        print(f'{idx}번째 : {matchId}의 데이터 추가')
        time.sleep(1.2)


def savePerMinDataset(dataset, fileName, idx):
    with open(fileName, 'a', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        if idx == 0:
            w.writeheader()
        w.writerow(dataset)


# 데이터 수집하다가 중간에 끊겼을 때 사용 (th에 최종 출력된 인덱스 번호 넣으면 됨)
def append_saveDataSetToCSV(matchIdSet, fileName, frame, th, tier):
    with open(fileName, 'a', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        i = th
        for matchId in matchIdSet:
            i += 1
            try:
                if i%2 == 0:
                    dic_data = getPerMinDataset.getResult(matchId, frame, 1, tier)
                else:
                    dic_data = getPerMinDataset.getResult(matchId, frame, 2, tier)
            except KeyError:
                print("KeyError발생.. 20초 대기 후 재시도.. ")
                time.sleep(20)
                try:
                    if i%2 == 0:
                        dic_data = getPerMinDataset.getResult(matchId, frame, 1, tier)
                    else:
                        dic_data = getPerMinDataset.getResult(matchId, frame, 2, tier)
                except KeyError:
                    continue
            if dic_data == 0:
                time.sleep(1.2)
                continue
            w.writerow(dic_data)
            print(f'{i} : {matchId}의 데이터 추가')
            time.sleep(1.2)