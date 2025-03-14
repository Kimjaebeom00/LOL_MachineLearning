import requests
import pprint
import numpy as np


pp = pprint.PrettyPrinter(indent=4)

# 24시간마다 변경해야 함
api_key = 'RGAPI-997afdec-aea4-4811-97ee-af7543a71cbb'
api_key2 = 'RGAPI-722f2ddc-edf4-48f1-a1ed-d6977ab876c0'

request_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
}
request_header2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key2
}

# 유저 puuid 가져오기
def getUserPuuid(summonerName):
    url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?{api_key}"
    return requests.get(url, headers=request_header).json()['puuid']
# print(get_userPuuid('청파소나타')['puuid'])

# SummonerId로 유저 puuid 가져오기
def getUserPuuidBySummonerId(SummonerId):
    url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/{SummonerId}?{api_key}"
    return requests.get(url, headers=request_header).json()['puuid']

# 게임 match_id 찾기
def getMatchId(puuid, start, count):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}"
    return requests.get(url, headers=request_header).json()
# pp.pprint(getMatchId("P4Ri8HBanEdTxQeT2cQS1MIN8RFQxaSukyHtFScjRLvUlzVMReZn_Rhzgzxr_HpZjxE_ah3fy4xaiA", 0, 10))

# 게임 정보 가져오기
def getGameInfo(matchId):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{matchId}"
    return requests.get(url, headers=request_header).json()
# pp.pprint(getGameInfo("KR_6710383118"))

def secondGetGameInfo(matchId):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{matchId}"
    return requests.get(url, headers=request_header2).json()

# 타임라인으로 게임 정보 가져오기
def getGameInfoTimeline(matchId):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{matchId}/timeline"
    return requests.get(url, headers=request_header).json()

def secondGetGameInfoTimeline(matchId):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{matchId}/timeline"
    return requests.get(url, headers=request_header2).json()

# 챌린저 소환사 정보 가져오기
def getChallengerEntries():

    url = f"https://kr.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key={api_key}"
    return requests.get(url, headers=request_header).json()['entries']

# 그랜드마스터 소환사 정보 가져오기
def getGrandmasterEntries():
    url = f"https://kr.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5?api_key={api_key}"
    return requests.get(url, headers=request_header).json()['entries']

# 마스터 소환사 정보 가져오기
def getMasterEntries():
    url = f"https://kr.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5?api_key={api_key}"
    return requests.get(url, headers=request_header).json()['entries'][:600]

# 티어별/페이지별 소환사 정보 가져오기
def getEntries(tier="PLATINUM", rank="IV", page=1):
    valid_tiers = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "EMERALD", "DIAMOND"]
    valid_ranks = ["IV", "III", "II", "I"]

    # 유효확인
    if tier not in valid_tiers:
        raise ValueError("재입력")
    url = f"https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/PLATINUM/{tier}?page={page}&api_key={api_key}"
    
    if rank not in valid_ranks:
        raise ValueError("재입력")

    url = f"https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{tier}/{rank}?page={page}&api_key{api_key}"
    return requests.get(url, headers=request_header).json()
    
# print(getChallengerEntries())
# print(getUserPuuid('BRO Morgan'))
# #BRO Morgan
# print(getMatchId('SAHqMCotWN0cg7n7pCDt4O7fLSnZAAttaN9CFhdSLvQoRk4aCCBGdC2fI2ON2WnMnMBtprwkj6mULQ',0,15))


if __name__=="__main__":
    import pandas as pd
    import csv
    import time
    
    # 분당 이벤트 갯수 가져오기
    gameData = pd.read_csv('Dataset/perMinuteDataset/10min/CHALLENGER.csv')
    matchId = gameData['matchId']
    matchId = matchId.iloc[0:1000]
    header = ['MatchId', '5min', '6min', '7min', '8min', '9min', '10min', '11min', '12min', '13min', '14min', '15min']
    for i in range(len(matchId)):
        result = {}
        result['MatchId'] = matchId[i]
        try:
            gameTimelineInfo = getGameInfoTimeline(matchId[i])['info']
        except KeyError:
            print("KeyError 발생 .. 10초 대기")
            time.sleep(10)
        for j in range(11):
            result[header[j+1]] = len(gameTimelineInfo['frames'][j+5]['events'])
        with open(f'event.csv', 'a', newline='') as f:
            w = csv.DictWriter(f, fieldnames=header)
            if i == 0:
                w.writeheader()
            w.writerow(result)
        print(f'{i}번째{result}: 추가')
        time.sleep(0.5)