from getData import getDataset
import csv
import time

fieldnames = [
        'matchId', # 매치아이디
        'queueId', # 큐 아이디 420 솔로랭크, 440 자유랭크
        'Diff_LV', # 총 레벨 차이
        'Diff_CS', # 총 미니언 킬 수 차이
        'Diff_jglCS', # 총 정글몹 킬 수 차이
        'Diff-K', # 총 킬 차이
        'Diff-K-top', # 탑 라이너 킬 차이
        'K-WIN-top', # 이긴 팀의 탑 라이너 킬
        'K-LOSE-top', # 진 팀의 탑 라이너 킬
        'Diff-K-jug', # 정글러 킬 차이
        'K-WIN-jug', # 이긴 팀의 정글러 킬
        'K-LOSE-jug', # 진 팀의 정글러 킬
        'Diff-K-mid', # 미드 라이너 킬 차이
        'K-WIN-mid', # 이긴 팀의 미드 라이너 킬
        'K-LOSE-mid', # 진 팀의 미드 라이너 킬
        'Diff-K-ad', # 원딜러 킬 차이
        'K-WIN-ad', # 이긴 팀의 원딜러 킬
        'K-LOSE-ad', # 진 팀의 원딜러 킬
        'Diff-K-sup', # 서포터 킬 차이
        'K-WIN-sup', # 이긴 팀의 서포터 킬
        'K-LOSE-sup', # 진 팀의 서포터 킬
        'invadeKill', # 미니언 생성(2분 5초) 전에 킬 발생 여부
        'Diff-A', # 총 어시스트 차이
        'Diff_WARDplaced', # 와드 설치 개수 차이
        'Diff-ControlWARDplaced', # 제어와드 설치 개수 차이
        'LOSE_controlWARDPlaced', # 진 팀의 제어와드 개수
        'WIN_controlWARDPlaced', # 이긴 팀의 제어와드 개수
        'Diff_WARDkill', # 와드 파괴 개수 차이
        'Diff_Inhibitor', # 파괴한 억제기 수 차이 
        'Diff_TOWERkill', # 파과한 타워 수 차이
        'Diff_FirstDRAGON', # 첫 용 획득 여부
        'Diff_FirstHERALD', # 첫 전령 획득 여부
        'Diff_Firsttower', # 첫 타워 제거 여부
        'Diff_FirstBLOOD', # 첫 킬 획득 여부
        'dragonType', # 1.바람 2.대지 3.화염 4.바다 5.마법공학 6.화학공학 7.장로
        'result' # 승리 1, 패배 -1
    ]
def saveDataSetToCSV(matchIdSet, fileName, frame):
    with open(fileName, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        i = 0
        for matchId in matchIdSet:
            i += 1
            dic_data = getDataset.getResult(matchId, frame)
            if dic_data == 0:
                time.sleep(2.5)
                continue
            w.writerow(dic_data)
            print(f'{i} : {matchId}의 데이터 추가')
            time.sleep(2.5)

# 데이터 수집하다가 중간에 끊겼을 때 사용 (th에 최종 출력된 인덱스 번호 넣으면 됨)
def append_saveDataSetToCSV(matchIdSet, fileName, frame, th):
    with open(fileName, 'a', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        i = th
        for matchId in matchIdSet:
            i += 1
            dic_data = getDataset.getResult(matchId, frame)
            if dic_data == 0:
                time.sleep(2.5)
                continue
            w.writerow(dic_data)
            print(f'{i} : {matchId}의 데이터 추가')
            time.sleep(2.5)