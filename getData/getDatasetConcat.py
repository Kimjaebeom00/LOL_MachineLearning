import pandas as pd

def Win_Lose_DataSet_Create(dataframe, filename):
    
    def save_win_dataframe_to_csv(dataframe, filename):
        df = pd.DataFrame(dataframe)
        df.to_csv(filename, index=False)
        
        
    #승리팀 DataSet 만드는 코드
    #1. 우선 승리팀의 티어(1~4)를 read한다.
  
    #티어별로 2600개씩 슬라이싱 -> 나중에 data1~data4 까지 병합한 이후에 중복제거 하면 10000개로 하면 부족할수있으므로 2600개씩 10400개 수집
    # data1 = data1.drop(data1.index[2600:])
    # data2 = data2.drop(data2.index[2600:])
    # data3 = data3.drop(data3.index[2600:])
    # data4 = data4.drop(data4.index[2600:])

    #데이터 병합하는 과정 및 중복검사 및 제거 keep='first'로 하면 중복되는 값이 있을 경우 처음꺼는 살리고 이후 중복값은 제거 하는 것.
    windata = dataframe
    windata = windata.drop_duplicates(subset=['matchId'], keep='first')
    windata = windata.iloc[:10000] # 10400개에서 중복제거하고 10000개로 슬라이싱
    compare = windata[windata['matchId'].duplicated(keep=False)] # 중복이 있는지 확인해주는 로직
    save_win_dataframe_to_csv(windata,f"../Dataset/perMinuteDataset/10min/{filename}_win.csv")
    print(windata)
    print(compare['matchId'])

