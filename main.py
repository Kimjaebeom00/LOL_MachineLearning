import pprint
import numpy as np
from getData import getAPI
from getData import getLoseDataset
from getData import getMatchId
import csv
#import saveDataset
import pandas as pd
#import secondSaveDataset
from saveData import saveLoseDataset
import pandas as pd
from getData import getDatasetConcat
from getData import getPerMinDataset
import etcFunction
from saveData import saveWinDataset

pp = pprint.PrettyPrinter(indent=4)


if __name__ == "__main__":
    #1st. matchId csv로 저장 (주석 해제)
    # tier = "SILVER" # 대문자 풀네임으로 작성
    # ranks = ["I", "II", "III", "IV"]
    # for rank in ranks:
    #     matchId = getMatchId.getMatchIdByTierAndRank(tier, rank, 1, 2)
    #     with open(f'MatchId/{tier}_{rank}.csv', 'w', newline='') as f:
    #         w = csv.writer(f)
    #         w.writerow(matchId)
    
    # 매치 아이디로 데이터셋 수집
    #  for rank in ranks:
    #      matchId = pd.read_csv(f'MatchId/{tier}_{rank}.csv')
    #      stopIndex = 3998 # 데이터 처음 수집할 때는 0으로 설정, 수집 중에 중단되면 콘솔에 찍힌 'a번째 : KR_6782605722의 데이터 추가'의 a를 stopIndex에 할당
    #      matchId = matchId.iloc[:, stopIndex:]
    #      saveWinDataset.saveDataSetToCSV(matchId, 15, tier, stopIndex)

    # 1.1 챌린저, 그마, 마스터 매치아이디 저장
    tier = "CHALLENGER" # 대문자 풀네임으로 작성
    # matchId = getMatchId.getChallengerMatchId()
    # with open(f'MatchId/{tier}_ver2.csv', 'w', newline='') as f:
    #     w = csv.writer(f)
    #     w.writerow(matchId)
    # print(getAPI.getMatchId('RqtD69lbQZFMNfo-P_i7bBnhkiy9aXdqNY5Q29Ms0ru4PyNVAB3byLycRZfjnNhHH63MLUOLgZncsw', 0, 10))

    # 챌린저, 그마, 마스터 저장
    matchId = pd.read_csv(f'MatchId/CHALLENGER.csv')
    stopIndex = 0 # 데이터 처음 수집할 때는 0으로 설정, 수집 중에 중단되면 콘솔에 찍힌 'a번째 : KR_6782605722의 데이터 추가'의 a를 stopIndex에 할당
    matchId = matchId.iloc[:, stopIndex:]
    saveWinDataset.saveDataSetToCSV(matchId, 15, tier, stopIndex)

    # 패배 데이터셋 만들기
    # Chanllenger_ver2 = pd.read_csv('Dataset/win_10/10_Grandmaster.csv')
    # saveLoseDataset.save_dataframe_to_csv(Chanllenger_ver2,'Dataset/lose_10/LvKA_10_Grandmaster.csv')

    # data 중복 제거, 10000개로 슬라이싱 후 저장
    # data1 = pd.read_csv("Dataset/win/Platinum_I.csv")
    # data2 = pd.read_csv("Dataset/win/Platinum_II.csv")
    # data3 = pd.read_csv("Dataset/win/Platinum_III.csv")
    # data4 = pd.read_csv("Dataset/win/Platinum_IV.csv")
    # getDatasetConcat.Win_Lose_DataSet_Create(data1,data2,data3,data4,'Platinum')

    # 5분부터 15분까지의 데이터 저장
    #getPerMinDataset.getResult('KR_6710383118', 15, 1, 'dia')


    # 게임 내의 participantId와 champion name 가져오기
    # id = 6751662212
    # gameTimelineInfo = getAPI.getGameInfoTimeline(f'KR_{id}')['info']
    # etcFunction.getParticipantId_ChampionName(f'KR_{id}')
    
