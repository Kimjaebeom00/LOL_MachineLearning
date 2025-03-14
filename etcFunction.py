import pprint
from getData import getAPI
import pandas as pd
import numpy as np
pp = pprint.PrettyPrinter(indent=4)

# 승리 팀, 패배 팀 participantId로 나누기
def teamClassfication(matchId):
    gameInfo = getAPI.getGameInfo(matchId)['info']['participants']
    winTeamMember = []
    loseTeamMember = []
    for i in range(1, 11):
        if gameInfo[i-1]['win'] == True:
            winTeamMember.append(gameInfo[i-1]['participantId'])
        elif gameInfo[i-1]['win'] == False:
            loseTeamMember.append(gameInfo[i-1]['participantId'])
    # if id in winTeamMember:
    #     return winTeamValue
    #     winTeamValue['wardCreatorId'].append(wardCreatorId)
    # elif wardCreatorId in loseTeamMember:
    #     loseTeamValue['wardCreatorId'].append(wardCreatorId)
    return winTeamMember, loseTeamMember

# 게임 내의 participantId와 champion name 가져오기
def getParticipantId_ChampionName(matchId):
    gameInfo = getAPI.getGameInfo(matchId)['info']
    for i in range(10):
        print(gameInfo['participants'][i]['participantId'])
        print(gameInfo['participants'][i]['summonerName'])
        print(gameInfo['participants'][i]['championName'])

# 처음 오브젝트 획득 한 팀
def whoFirstGet(firstObjectInfo, object):
    if firstObjectInfo[0]['objectives'][object]['first']:
        return firstObjectInfo[0]['win']
    elif firstObjectInfo[1]['objectives'][object]['first']:
        return firstObjectInfo[1]['win']
    
    
def Win_Lose_DataSet_Create(dataframe1, dataframe2, dataframe3, dataframe4, filename):
    
    def save_win_dataframe_to_csv(dataframe, filename):
        dataframe.to_csv(filename, index=False)
    
    def save_lose_dataframe_to_csv(dataframe, filename):
        df = pd.DataFrame(dataframe)
        columns_to_exclude_index = [0, 1, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 26, 34]  
        columns_to_multiply_by_minus_1_index = [col_idx for col_idx in range(len(df.columns)) if col_idx not in columns_to_exclude_index]
        df.iloc[:, columns_to_multiply_by_minus_1_index] = df.iloc[:, columns_to_multiply_by_minus_1_index] * -1
        df.to_csv(filename, index=False)

    # 승리팀 DataSet 만드는 코드
    data1 = pd.read_csv(f"Dataset/win/{dataframe1}")
    data2 = pd.read_csv(f"Dataset/win/{dataframe2}")
    data3 = pd.read_csv(f"Dataset/win/{dataframe3}")
    data4 = pd.read_csv(f"Dataset/win/{dataframe4}")

    # 티어별로 2600개씩 슬라이싱 -> 나중에 data1~data4까지 병합한 이후에 중복 제거하면 10000개로 하면 부족할 수 있으므로 2600개씩 10400개 수집
    data1 = data1.drop(data1.index[2600:])
    data2 = data2.drop(data2.index[2600:])
    data3 = data3.drop(data3.index[2600:])
    data4 = data4.drop(data4.index[2600:])

    # 데이터 병합하는 과정 및 중복 검사 및 제거. keep='first'로 하면 중복되는 값이 있을 경우 처음 것은 살리고 이후 중복값은 제거하는 것.
    windata = pd.concat([data1, data2, data3, data4])
    windata = windata.drop_duplicates(subset=['matchId'], keep='first')
    windata = windata.iloc[:10000] # 10400개에서 중복 제거하고 10000개로 슬라이싱
    compare = windata[windata['matchId'].duplicated(keep=False)] # 중복이 있는지 확인해주는 로직
    save_win_dataframe_to_csv(windata, f"Dataset/win/{filename}_win.csv")
    print(windata)
    print(compare['matchId'])

    #패배팀 DataSet 생성
    losedata = windata.copy() # 승리팀 10000개 DataSet을 그대로 가져와서 거기에 -1만 곱해주면 끝.
    save_lose_dataframe_to_csv(losedata,"Dataset/lose/{filename}_lose.csv") #-1 곱해주고 저장해주는 함수


    

def tempLoadData(frameNum, gameTimelineInfo, winTeamMember, winTeamValue, loseTeamMember, loseTeamValue, dataSet, KillerIdList, victimIdList):
    # 레벨, 미니언 킬, 정글몹 킬 구하기
    for i in range(1, 11):
        participantFrames = gameTimelineInfo['frames'][frameNum]['participantFrames'][str(i)]
        if i in winTeamMember:
            if i == 1 or i == 6:
                dataSet['WIN_LV_top'] = participantFrames['level']
                dataSet['WIN_CS_top'] = participantFrames['minionsKilled']
                dataSet['WIN_jglCS_top'] = participantFrames['jungleMinionsKilled']
                dataSet['WIN_GOLD_top'] = participantFrames['totalGold']
                dataSet['WIN_Kill_top'] = KillerIdList.count(i)
                dataSet['WIN_Death_top'] = victimIdList.count(i)
            if i == 2 or i == 7:
                dataSet['WIN_LV_jgl'] = participantFrames['level']
                dataSet['WIN_CS_jgl'] = participantFrames['minionsKilled']
                dataSet['WIN_jglCS_jgl'] = participantFrames['jungleMinionsKilled']
                dataSet['WIN_GOLD_jgl'] = participantFrames['totalGold']
                dataSet['WIN_Kill_jgl'] = KillerIdList.count(i)
                dataSet['WIN_Death_jgl'] = victimIdList.count(i)
            if i == 3 or i == 8:
                dataSet['WIN_LV_mid'] = participantFrames['level']
                dataSet['WIN_CS_mid'] = participantFrames['minionsKilled']
                dataSet['WIN_jglCS_mid'] = participantFrames['jungleMinionsKilled']
                dataSet['WIN_GOLD_mid'] = participantFrames['totalGold']
                dataSet['WIN_Kill_mid'] = KillerIdList.count(i)
                dataSet['WIN_Death_mid'] = victimIdList.count(i)
            if i == 4 or i == 9:
                dataSet['WIN_LV_ad'] = participantFrames['level']
                dataSet['WIN_CS_ad'] = participantFrames['minionsKilled']
                dataSet['WIN_jglCS_ad'] = participantFrames['jungleMinionsKilled']
                dataSet['WIN_GOLD_ad'] = participantFrames['totalGold']
                dataSet['WIN_Kill_ad'] = KillerIdList.count(i)
                dataSet['WIN_Death_ad'] = victimIdList.count(i)
            if i == 5 or i == 10:
                dataSet['WIN_LV_sup'] = participantFrames['level']
                dataSet['WIN_CS_sup'] = participantFrames['minionsKilled']
                dataSet['WIN_jglCS_sup'] = participantFrames['jungleMinionsKilled']
                dataSet['WIN_GOLD_sup'] = participantFrames['totalGold']
                dataSet['WIN_Kill_sup'] = KillerIdList.count(i)
                dataSet['WIN_Death_sup'] = victimIdList.count(i)
        elif i in loseTeamMember:
            if i == 1 or i == 6:
                dataSet['LOSE_LV_top'] = participantFrames['level']
                dataSet['LOSE_CS_top'] = participantFrames['minionsKilled']
                dataSet['LOSE_jglCS_top'] = participantFrames['jungleMinionsKilled']
                dataSet['LOSE_GOLD_top'] = participantFrames['totalGold']
                dataSet['LOSE_Kill_top'] = KillerIdList.count(i)
                dataSet['LOSE_Death_top'] = victimIdList.count(i)
            if i == 2 or i == 7:
                dataSet['LOSE_LV_jgl'] = participantFrames['level']
                dataSet['LOSE_CS_jgl'] = participantFrames['minionsKilled']
                dataSet['LOSE_jglCS_jgl'] = participantFrames['jungleMinionsKilled']
                dataSet['LOSE_GOLD_jgl'] = participantFrames['totalGold']
                dataSet['LOSE_Kill_jgl'] = KillerIdList.count(i)
                dataSet['LOSE_Death_jgl'] = victimIdList.count(i)
            if i == 3 or i == 8:
                dataSet['LOSE_LV_mid'] = participantFrames['level']
                dataSet['LOSE_CS_mid'] = participantFrames['minionsKilled']
                dataSet['LOSE_jglCS_mid'] = participantFrames['jungleMinionsKilled']
                dataSet['LOSE_GOLD_mid'] = participantFrames['totalGold']
                dataSet['LOSE_Kill_mid'] = KillerIdList.count(i)
                dataSet['LOSE_Death_mid'] = victimIdList.count(i)
            if i == 4 or i == 9:
                dataSet['LOSE_LV_ad'] = participantFrames['level']
                dataSet['LOSE_CS_ad'] = participantFrames['minionsKilled']
                dataSet['LOSE_jglCS_ad'] = participantFrames['jungleMinionsKilled']
                dataSet['LOSE_GOLD_ad'] = participantFrames['totalGold']
                dataSet['LOSE_Kill_ad'] = KillerIdList.count(i)
                dataSet['LOSE_Death_ad'] = victimIdList.count(i)
            if i == 5 or i == 10:
                dataSet['LOSE_LV_sup'] = participantFrames['level']
                dataSet['LOSE_CS_sup'] = participantFrames['minionsKilled']
                dataSet['LOSE_jglCS_sup'] = participantFrames['jungleMinionsKilled']
                dataSet['LOSE_GOLD_sup'] = participantFrames['totalGold']
                dataSet['LOSE_Kill_sup'] = KillerIdList.count(i)
                dataSet['LOSE_Death_sup'] = victimIdList.count(i)

    # 0번 인덱스의 diffKillScore에 관한 어시스트는 diffAssistScore의 0번 인덱스임
    for i in winTeamValue['killInfo']['assistId']:
        if i != None:
            for j in i:
                if j == 1 or j == 6:
                    dataSet['WIN_Asisst_top'] += i.count(j)
                if j == 2 or j == 7:
                    dataSet['WIN_Asisst_jgl'] += i.count(j)
                if j == 3 or j == 8:
                    dataSet['WIN_Asisst_mid'] += i.count(j)
                if j == 4 or j == 9:
                    dataSet['WIN_Asisst_ad'] += i.count(j)
                if j == 5 or j == 10:
                    dataSet['WIN_Asisst_sup'] += i.count(j)
    for i in loseTeamValue['killInfo']['assistId']:
        if i != None:
            for j in i:
                if j == 1 or j == 6:
                    dataSet['LOSE_Asisst_top'] += i.count(j)
                if j == 2 or j == 7:
                    dataSet['LOSE_Asisst_jgl'] += i.count(j)
                if j == 3 or j == 8:
                    dataSet['LOSE_Asisst_mid'] += i.count(j)
                if j == 4 or j == 9:
                    dataSet['LOSE_Asisst_ad'] += i.count(j)
                if j == 5 or j == 10:
                    dataSet['LOSE_Asisst_sup'] += i.count(j)
    dataSet['WIN_WARDplaced'] = len(winTeamValue['wardCreatorId'])
    dataSet['LOSE_WARDplaced'] = len(loseTeamValue['wardCreatorId'])
    dataSet['WIN_WARDkill'] = len(winTeamValue['wardKillerId'])
    dataSet['LOSE_WARDkill'] = len(loseTeamValue['wardKillerId'])
    dataSet['WIN_Inhibitor'] = len(winTeamValue['inhibitorBreakerId'])
    dataSet['LOSE_Inhibitor'] = len(loseTeamValue['inhibitorBreakerId'])
    dataSet['WIN_TOWERkill'] = len(winTeamValue['towerBreakerId'])
    dataSet['LOSE_TOWERkill'] = len(loseTeamValue['towerBreakerId'])
    return dataSet

def delete_or_add_header(tier):
    header = ['queueId', 'matchId', 'Diff_FirstBLOOD', 'Diff_FirstDRAGON', 'Diff_FirstHERALD', 'Diff_Firsttower', 'dragonType', 
              'WIN_invadeKill', 'LOSE_invadeDeath', 'LOSE_invadeKill', 'WIN_invadeDeath', 'WIN_controlWARDPlaced', 'LOSE_controlWARDPlaced',
              'WIN_Kill_top','WIN_Kill_jgl','WIN_Kill_mid','WIN_Kill_ad','WIN_Kill_sup','LOSE_Kill_top','LOSE_Kill_jgl','LOSE_Kill_mid',
              'LOSE_Kill_ad','LOSE_Kill_sup','WIN_Death_top','WIN_Death_jgl','WIN_Death_mid','WIN_Death_ad','WIN_Death_sup','LOSE_Death_top','LOSE_Death_jgl',
              'LOSE_Death_mid','LOSE_Death_ad','LOSE_Death_sup','WIN_Asisst_top','WIN_Asisst_jgl','WIN_Asisst_mid','WIN_Asisst_ad','WIN_Asisst_sup',
              'LOSE_Asisst_top','LOSE_Asisst_jgl','LOSE_Asisst_mid','LOSE_Asisst_ad','LOSE_Asisst_sup','WIN_LV_top','WIN_LV_jgl','WIN_LV_mid','WIN_LV_ad',
              'WIN_LV_sup','LOSE_LV_top','LOSE_LV_jgl','LOSE_LV_mid','LOSE_LV_ad','LOSE_LV_sup','WIN_CS_top','WIN_CS_jgl','WIN_CS_mid','WIN_CS_ad',
              'WIN_CS_sup','LOSE_CS_top','LOSE_CS_jgl','LOSE_CS_mid','LOSE_CS_ad','LOSE_CS_sup','WIN_jglCS_top','WIN_jglCS_jgl','WIN_jglCS_mid',
              'WIN_jglCS_ad','WIN_jglCS_sup','LOSE_jglCS_top','LOSE_jglCS_jgl','LOSE_jglCS_mid','LOSE_jglCS_ad','LOSE_jglCS_sup','WIN_GOLD_top','WIN_GOLD_jgl',
              'WIN_GOLD_mid','WIN_GOLD_ad','WIN_GOLD_sup','LOSE_GOLD_top','LOSE_GOLD_jgl','LOSE_GOLD_mid','LOSE_GOLD_ad','LOSE_GOLD_sup','WIN_WARDkill',
              'LOSE_WARDkill','WIN_Inhibitor','LOSE_Inhibitor','WIN_TOWERkill','LOSE_TOWERkill','WIN_WARDplaced','LOSE_WARDplaced']
    for min in range(5, 16):
        df = pd.read_csv(f'Dataset/perMinuteDataset/{min}min/{tier}.csv')
        dfPath = f'Dataset/perMinuteDataset/{min}min/{tier}.csv'
        if df.columns[1][0:2] == 'KR':
            df = pd.read_csv(f'Dataset/perMinuteDataset/{min}min/{tier}.csv', names=header)
            df.to_csv(dfPath, index=False)
        print('min : ', min)
        result = df[df['queueId'] == 'queueId']
        for j in result.index:
            df= df.drop(j, axis=0)
        df.to_csv(dfPath, index=False)

# 매치 아이디 중복 제거
def remove_duplicates_matchId(tier):
    df = pd.read_csv(f"/MatchId/{tier}.csv", header=None)
    df_transposed = df.transpose()
    print(df_transposed.shape)
    df_transposed_dup = df_transposed.drop_duplicates()
    print(df_transposed_dup.shape)
    result = df_transposed_dup.transpose()
    result.to_csv(f'/MatchId/{tier}.csv', index=False, header=False)


if __name__ == "__main__":
    dfA = pd.read_csv(f"MatchId/CHALLENGER.csv", header=None)
    dfB = pd.read_csv(f"MatchId/ChanllengerMatchId.csv", header=None)
    df = pd.concat([dfA, dfB], ignore_index=True, axis=1)
    df_transposed = df.transpose()
    print(df_transposed.shape)
    df_transposed_dup = df_transposed.drop_duplicates(keep=False)
    print(df_transposed_dup.shape)
    result = df_transposed_dup.transpose()
    result.to_csv(f"MatchId/CHALLENGER.csv", index=False, header=False)