import time
from getData import getAPI

# KeyError: 'puuid' 발생 시 time.sleep(n)값 증가

# 챌린저 matchId 가져오기(약 6분 / 3,000 데이터)
def getChallengerMatchId():
    challengerMatchIdSet = set()
    # 챌린저 소환사 Puuid 가져오기(중복제거)
    for entry in getAPI.getChallengerEntries():
        print("챌린저 matchId 가져오는 중 ... ")
        challengerMatchIdSet.update(getAPI.getMatchId(getAPI.getUserPuuidBySummonerId(entry['summonerId']), 0, 20))
        time.sleep(0.7)
    return challengerMatchIdSet

# 그랜드마스터 matchId 가져오기(약 14분 / 8,000 데이터)
def getGrandmasterMatchId():
    grandmasterMatchIdSet = set()

    # 그랜드마스터 소환사 Puuid 가져오기(중복제거)
    for entry in getAPI.getGrandmasterEntries():
        grandmasterMatchIdSet.update(getAPI.getMatchId(getAPI.getUserPuuidBySummonerId(entry['summonerId']), 0, 20))
        time.sleep(0.7)

    return grandmasterMatchIdSet

# 마스터 matchId 가져오기(약 30분(?) / 11,000 데이터)
def getMasterMatchId():
    masterMatchIdSet = set()
    # 마스터 소환사 Puuid 가져오기(중복제거)
    for entry in getAPI.getMasterEntries():
        masterMatchIdSet.update(getAPI.getMatchId(getAPI.getUserPuuidBySummonerId(entry['summonerId']), 0, 20))
        time.sleep(0.7)

    return masterMatchIdSet


def getMatchIdByTierAndRank(tier, rank, start_page, end_page, matchid_num=5000): #matchid_num은 몇개의 매치아이디를 가져올지 정하는 변수
    matchIdSet = set()
    matchid_total = 0  # 가져온 matchid 수를 추적

    for page in range(start_page, end_page + 1):
        for entry in getAPI.getEntries(tier, rank, page):
            if matchid_total >= matchid_num:
                break  # 원하는 matchid 수에 도달하면 루프 종료
            matchids = getAPI.getMatchId(getAPI.getUserPuuidBySummonerId(entry['summonerId']), 0, 20)
            matchid_count = len(matchids)
            if matchid_total + matchid_count <= matchid_num:
                matchIdSet.update(matchids)
                matchid_total += matchid_count
            else:
                # matchid_num을 초과하지 않도록 일부 matchids만 추가
                max_matchids = matchid_num - matchid_total # 현재 가져온 매치아이디에서 matchid_total빼서 즉 아직 가져와야 할 매치아이디를 개수를 넣어줌
                matchIdSet.update(matchids[:max_matchids])
                matchid_total = matchid_num
            time.sleep(0.7)

        if matchid_total >= matchid_num:
            break  # 지정한 match ID 갯수에 도달하면 종료~~

    return matchIdSet

if __name__ == "__main__":
    match_ids = getMatchIdByTierAndRank("BRONZE", "I", 1, 1)  #원하는 티어, 랭크, 페이지 시작, 페이지 종료 값 입력
    print(match_ids)
    
    

