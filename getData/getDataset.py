import pprint
import numpy as np
from getData import getAPI
import etcFunction as ef

pp = pprint.PrettyPrinter(indent=4)

'''
포블 데이터 추가
드래곤 타입 추가
'WIN' -> int형으로 바꾸기
1분 30초 이전에 킬이 발생했는지 = bool

'''

# 15분 후 게임 데이터 셋
def getResult(matchId, frame, count):
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
    # elif (gameInfo['gameDuration']/60) < frame:
    #     print(f'{int(gameInfo["gameDuration"]/60)}분 만에 끝난 게임이어서 데이터 셋에 추가되지 않음')
    #     return 0
    winTeamMember = []
    loseTeamMember = []
    for i in range(1, 11):
        if gameInfo['participants'][i-1]['win'] == True:
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
    dataSet['invadeKill'] = 0
    dataSet['WIN_controlWARDPlaced'] = 0
    dataSet['LOSE_controlWARDPlaced'] = 0
    dataSet['Diff-ControlWARDplaced'] = 0
    dataSet['K-WIN-top'] = 0
    dataSet['K-WIN-jug'] = 0
    dataSet['K-WIN-mid'] = 0
    dataSet['K-WIN-ad'] = 0
    dataSet['K-WIN-sup'] = 0
    dataSet['K-LOSE-top'] = 0
    dataSet['K-LOSE-jug'] = 0
    dataSet['K-LOSE-mid'] = 0
    dataSet['K-LOSE-ad'] = 0
    dataSet['K-LOSE-sup'] = 0
    KillerIdList = []
    # frame을 '분' 단위로 치환하기 위해 +1
    # 15분 이전 예외처리
    for i in range(frame+1):
        events = gameTimelineInfo['frames'][i]['events']
        for j in range(len(events)):
            # 킬/어시
            if events[j]['type'] == 'CHAMPION_KILL':
                killerId = events[j]['killerId']
                assistId = None
                KillerIdList.append(killerId)
                if events[j]['timestamp'] < 125000:
                    if killerId in winTeamMember:
                        dataSet['invadeKill'] += 1
                    elif killerId in loseTeamMember:
                        dataSet['invadeKill'] += -1
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
    # 레벨, 미니언 킬, 정글몹 킬 구하기
    for i in range(1, 11):
        participantFrames = gameTimelineInfo['frames'][frame]['participantFrames'][str(i)]
        if i in winTeamMember:
            winTeamValue['level'].append(participantFrames['level'])
            winTeamValue['minionsKilled'].append(participantFrames['minionsKilled'])
            winTeamValue['jungleMinionsKilled'].append(participantFrames['jungleMinionsKilled'])
        elif i in loseTeamMember:
            loseTeamValue['level'].append(participantFrames['level'])
            loseTeamValue['minionsKilled'].append(participantFrames['minionsKilled'])
            loseTeamValue['jungleMinionsKilled'].append(participantFrames['jungleMinionsKilled'])

    dataSet['Diff_LV'] = sum(np.array(winTeamValue['level']) - np.array(loseTeamValue['level']))
    dataSet['Diff_CS'] = sum(np.array(winTeamValue['minionsKilled']) - np.array(loseTeamValue['minionsKilled']))
    dataSet['Diff_jglCS'] = sum(np.array(winTeamValue['jungleMinionsKilled']) - np.array(loseTeamValue['jungleMinionsKilled']))
    # 0번 인덱스의 diffKillScore에 관한 어시스트는 diffAssistScore의 0번 인덱스임
    dataSet['Diff-K'] = len(winTeamValue['killInfo']['killerId']) - len(loseTeamValue['killInfo']['killerId'])
    dataSet['Diff-K-top'] = KillerIdList.count(1) - KillerIdList.count(6) 
    dataSet['Diff-K-jug'] = KillerIdList.count(2) - KillerIdList.count(7) 
    dataSet['Diff-K-mid'] = KillerIdList.count(3) - KillerIdList.count(8) 
    dataSet['Diff-K-ad'] = KillerIdList.count(4) - KillerIdList.count(9) 
    dataSet['Diff-K-sup'] = KillerIdList.count(5) - KillerIdList.count(10) 
    if 6 in winTeamMember:
        dataSet['Diff-K-top'] *= -1
        dataSet['Diff-K-jug'] *= -1
        dataSet['Diff-K-mid'] *= -1
        dataSet['Diff-K-ad'] *= -1
        dataSet['Diff-K-sup'] *= -1
    for i in range(1, 11):
        if i in winTeamMember:
            if i == 1 or i == 6:
                dataSet['K-WIN-top'] = KillerIdList.count(i)
            if i == 2 or i == 7:
                dataSet['K-WIN-jug'] = KillerIdList.count(i)
            if i == 3 or i == 8:
                dataSet['K-WIN-mid'] = KillerIdList.count(i)
            if i == 4 or i == 9:
                dataSet['K-WIN-ad'] = KillerIdList.count(i)
            if i == 5 or i == 10:
                dataSet['K-WIN-sup'] = KillerIdList.count(i)
        elif i in loseTeamMember:
            if i == 1 or i == 6:
                dataSet['K-LOSE-top'] = KillerIdList.count(i)
            if i == 2 or i == 7:
                dataSet['K-LOSE-jug'] = KillerIdList.count(i)
            if i == 3 or i == 8:
                dataSet['K-LOSE-mid'] = KillerIdList.count(i)
            if i == 4 or i == 9:
                dataSet['K-LOSE-ad'] = KillerIdList.count(i)
            if i == 5 or i == 10:
                dataSet['K-LOSE-sup'] = KillerIdList.count(i)
    dataSet['Diff-A'] = sum(len(i) for i in winTeamValue['killInfo']['assistId'] if i != None) - sum(len(i) for i in loseTeamValue['killInfo']['assistId'] if i != None)
    dataSet['Diff_WARDplaced'] = len(winTeamValue['wardCreatorId']) - len(loseTeamValue['wardCreatorId'])
    dataSet['Diff_WARDkill'] = len(winTeamValue['wardKillerId']) - len(loseTeamValue['wardKillerId'])
    dataSet['Diff_Inhibitor'] = len(winTeamValue['inhibitorBreakerId']) - len(loseTeamValue['inhibitorBreakerId'])
    dataSet['Diff_TOWERkill'] = len(winTeamValue['towerBreakerId']) - len(loseTeamValue['towerBreakerId'])
    dataSet['Diff-ControlWARDplaced'] = dataSet['WIN_controlWARDPlaced'] - dataSet['LOSE_controlWARDPlaced']
    dataSet['result'] = 1
    
    return dataSet