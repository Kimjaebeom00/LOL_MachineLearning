import sys
sys.path.append('.')
import pprint
import numpy as np
from getData import getAPI
import csv
import pandas as pd
import time
import etcFunction as ef
from saveData import saveWinDataset

pp = pprint.PrettyPrinter(indent=4)

'''
포블 데이터 추가
드래곤 타입 추가
'WIN' -> int형으로 바꾸기
1분 30초 이전에 킬이 발생했는지 = bool

'''

# 15분 후 게임 데이터 셋
def getResult(matchId, frame, count, tier, idx):
    print(f'{matchId}의 데이터 가져오는 중...')
    if count == 1:
        gameInfo = getAPI.getGameInfo(matchId)['info']
        gameTimelineInfo = getAPI.getGameInfoTimeline(matchId)['info']
    elif count == 2:
        gameInfo = getAPI.secondGetGameInfo(matchId)['info']
        gameTimelineInfo = getAPI.secondGetGameInfoTimeline(matchId)['info']
    if gameInfo['queueId'] != 420 and gameInfo['queueId'] != 440:
        print('솔로랭크 또는 자유랭크가 아닙니다.')
        return 0
    elif (gameInfo['gameDuration']/60) < frame:
        print(f'{int(gameInfo["gameDuration"]/60)}분 만에 끝난 게임이어서 데이터 셋에 추가되지 않음')
        return 0
    winTeamMember = []
    loseTeamMember = []
    for i in range(1, 11):
        if gameInfo['participants'][i-1]['win'] == True: #participants은 참가자들. (player 10명 이니깐 for문으로 10번 진행)
            winTeamMember.append(gameInfo['participants'][i-1]['participantId'])
        elif gameInfo['participants'][i-1]['win'] == False:
            loseTeamMember.append(gameInfo['participants'][i-1]['participantId'])
    winTeamValue = {'level' : [], 
                    'minionsKilled' : [], 
                    'jungleMinionsKilled' : [], 
                    'killInfo' : {'killerId' : [], 'assistId' : []}, 
                    'wardCreatorId' : [], 
                    'wardKillerId' : [],
                    'inhibitorBreakerId' : [],
                    'towerBreakerId' : [],
                    'dragonKill' : [],
                    'riftheraldKill' : []}
    loseTeamValue = {'level' : [], 
                     'minionsKilled' : [], 
                     'jungleMinionsKilled' : [], 
                     'killInfo' : {'killerId' : [], 'assistId' : []}, 
                     'wardCreatorId' : [], 
                     'wardKillerId' : [],
                     'inhibitorBreakerId' : [],
                     'towerBreakerId' : [],
                     'dragonKill' : [],
                     'riftheraldKill' : []}
    dataSet = {}
    dataSet['queueId'] = gameInfo['queueId']
    dataSet['matchId'] = matchId
    dataSet['Diff_FirstBLOOD'] = 0
    dataSet['Diff_FirstDRAGON'] = 0
    dataSet['Diff_FirstHERALD'] = 0
    dataSet['Diff_Firsttower'] = 0
    dataSet['dragonType'] = 0
    dataSet['WIN_invadeKill'] = 0
    dataSet['LOSE_invadeDeath'] = 0
    dataSet['LOSE_invadeKill'] = 0
    dataSet['WIN_invadeDeath'] = 0
    dataSet['WIN_controlWARDPlaced'] = 0
    dataSet['LOSE_controlWARDPlaced'] = 0
    dataSet['WIN_Kill_top'] = 0
    dataSet['WIN_Kill_jgl'] = 0
    dataSet['WIN_Kill_mid'] = 0
    dataSet['WIN_Kill_ad'] = 0
    dataSet['WIN_Kill_sup'] = 0
    dataSet['LOSE_Kill_top'] = 0
    dataSet['LOSE_Kill_jgl'] = 0
    dataSet['LOSE_Kill_mid'] = 0
    dataSet['LOSE_Kill_ad'] = 0
    dataSet['LOSE_Kill_sup'] = 0
    dataSet['WIN_Asisst_top'] = 0
    dataSet['WIN_Asisst_jgl'] = 0
    dataSet['WIN_Asisst_mid'] = 0
    dataSet['WIN_Asisst_ad'] = 0
    dataSet['WIN_Asisst_sup'] = 0
    dataSet['LOSE_Asisst_top'] = 0
    dataSet['LOSE_Asisst_jgl'] = 0
    dataSet['LOSE_Asisst_mid'] = 0
    dataSet['LOSE_Asisst_ad'] = 0
    dataSet['LOSE_Asisst_sup'] = 0
    killerIdList = []
    victimIdList = []
    # frame을 '분' 단위로 치환하기 위해 +1
    # 15분 이전 예외처리
    for i in range(frame+1):
        events = gameTimelineInfo['frames'][i]['events']
        for j in range(len(events)):
            # 킬/어시
            if events[j]['type'] == 'CHAMPION_KILL':
                killerId = events[j]['killerId']
                victimId = events[j]['victimId']
                assistId = None
                killerIdList.append(killerId)
                victimIdList.append(victimId)
                if events[j]['timestamp'] < 125000:
                    if killerId in winTeamMember:
                        dataSet['WIN_invadeKill'] += 1
                        dataSet['LOSE_invadeDeath'] += 1
                    elif killerId in loseTeamMember:
                        dataSet['LOSE_invadeKill'] += 1
                        dataSet['WIN_invadeDeath'] += 1
                if dataSet['Diff_FirstBLOOD'] == 0:
                    for k in range(2):
                        if gameInfo['teams'][k]['win']:
                            dataSet['Diff_FirstBLOOD'] = 1 if gameInfo['teams'][k]['objectives']['champion']['first'] else -1
                if 'assistingParticipantIds' in events[j]:
                    assistId = events[j]['assistingParticipantIds']
                if killerId in winTeamMember:
                    winTeamValue['killInfo']['killerId'].append(killerId)
                    winTeamValue['killInfo']['assistId'].append(assistId)
                elif killerId in loseTeamMember:
                    loseTeamValue['killInfo']['killerId'].append(killerId)
                    loseTeamValue['killInfo']['assistId'].append(assistId)
            # 와드 설치
            # 자이라의 식물도 와드로 식별됨.. 아마?
            if events[j]['type'] == 'WARD_PLACED':
                wardCreatorId = events[j]['creatorId']
                if wardCreatorId in winTeamMember:
                    winTeamValue['wardCreatorId'].append(wardCreatorId)
                    if events[j]['wardType'] == 'CONTROL_WARD':
                        dataSet['WIN_controlWARDPlaced'] += 1
                elif wardCreatorId in loseTeamMember:
                    loseTeamValue['wardCreatorId'].append(wardCreatorId)
                    if events[j]['wardType'] == 'CONTROL_WARD':
                        dataSet['LOSE_controlWARDPlaced'] += 1
            # 와드 파괴
            if events[j]['type'] == 'WARD_KILL':
                wardKillerId = events[j]['killerId']
                if wardKillerId in winTeamMember:
                    winTeamValue['wardKillerId'].append(wardKillerId)
                elif wardKillerId in loseTeamMember:
                    loseTeamValue['wardKillerId'].append(wardKillerId)


            # 구조물 파괴
            if events[j]['type'] == 'BUILDING_KILL':
                # 억제기
                if events[j]['buildingType'] == 'INHIBITOR_BUILDING':
                    buildingKillerId = events[j]['killerId']
                    if buildingKillerId in winTeamMember:
                        winTeamValue['inhibitorBreakerId'].append(buildingKillerId)
                    elif buildingKillerId in loseTeamMember:
                        loseTeamValue['inhibitorBreakerId'].append(buildingKillerId)
                # 타워
                if events[j]['buildingType'] == 'TOWER_BUILDING':
                    for k in range(2):
                        if gameInfo['teams'][k]['win']:
                            dataSet['Diff_Firsttower'] = 1 if gameInfo['teams'][k]['objectives']['tower']['first'] else -1
                    buildingKillerId = events[j]['killerId']
                    if buildingKillerId in winTeamMember:
                        winTeamValue['towerBreakerId'].append(buildingKillerId)
                    elif buildingKillerId in loseTeamMember:
                        loseTeamValue['towerBreakerId'].append(buildingKillerId)
            # 엘리트 몬스터 킬
            if events[j]['type'] == 'ELITE_MONSTER_KILL':
                # 드래곤
                if events[j]['monsterType'] == 'DRAGON':
                    mosterKillerId = events[j]['killerId']
                    if dataSet['dragonType'] == 0:
                        if events[j]['monsterSubType'] == 'AIR_DRAGON':
                            dataSet['dragonType'] = 1
                        elif events[j]['monsterSubType'] == 'EARTH_DRAGON':
                            dataSet['dragonType'] = 2
                        elif events[j]['monsterSubType'] == 'FIRE_DRAGON':
                            dataSet['dragonType'] = 3
                        elif events[j]['monsterSubType'] == 'WATER_DRAGON':
                            dataSet['dragonType'] = 4
                        elif events[j]['monsterSubType'] == 'HEXTECH_DRAGON':
                            dataSet['dragonType'] = 5
                        elif events[j]['monsterSubType'] == 'CHEMTECH_DRAGON':
                            dataSet['dragonType'] = 6
                    for k in range(2):
                        if gameInfo['teams'][k]['win']:
                            dataSet['Diff_FirstDRAGON'] = 1 if gameInfo['teams'][k]['objectives']['dragon']['first'] else -1
                # 전령
                if events[j]['monsterType'] == 'RIFTHERALD':
                    for k in range(2):
                        if gameInfo['teams'][k]['win']:
                            dataSet['Diff_FirstHERALD'] = 1 if gameInfo['teams'][k]['objectives']['riftHerald']['first'] else -1
        if i >= 5 and i <= 15: # 5 ~ 15분 데이터 저장
            dataSet = ef.tempLoadData(i, gameTimelineInfo, winTeamMember, winTeamValue, loseTeamMember, loseTeamValue, dataSet, killerIdList, victimIdList)
            fileName = f'Dataset/perMinuteDataset/{i}min/{tier}_ver2.csv'
            saveWinDataset.savePerMinDataset(dataSet, fileName, idx)
            # print(f'{i}분 : {matchId}의 데이터 추가')
    return dataSet


def getLengthEvent(tier):
    # 분당 이벤트 갯수 가져오기
    data = pd.read_csv(f'Dataset/perMinuteDataset/10min/{tier}.csv')
    matchId = data['matchId']
    matchId = matchId.iloc[0:1000]
    header = ['MatchId', '5min', '6min', '7min', '8min', '9min', '10min', '11min', '12min', '13min', '14min', '15min']
    for i in range(len(matchId)):
        result = {}
        result['MatchId'] = matchId[i]
        try:
            if i%2 == 0:
                gameTimelineInfo = getAPI.secondGetGameInfoTimeline(matchId[i])['info']
            else:
                gameTimelineInfo = getAPI.getGameInfoTimeline(matchId[i])['info']
        except KeyError:
            print("KeyError 발생 .. 20초 대기")
            time.sleep(20)
        for j in range(11):
            result[header[j+1]] = len(gameTimelineInfo['frames'][j+5]['events'])
        with open(f'Dataset/perMinuteDataset/result/event/{tier}.csv', 'a', newline='') as f:
            w = csv.DictWriter(f, fieldnames=header)
            if i == 0:
                w.writeheader()
            w.writerow(result)
        print(f'{i}번째{result}: 추가')
        time.sleep(0.2)

if __name__=="__main__":
    getLengthEvent("IRON")