import pandas as pd

def load_dataset(file):
    
    # 결측치 때문에 숫자로 변환이 안된다.
    raw_data = pd.read_csv(file, converters={"거치대수(LCD)": lambda x: str(x), "거치대수(QR)": lambda x: str(x)})
    
    print(raw_data.info())  # 2762 행
    
    # 마지막 copy()에 주의
    local_data = raw_data[raw_data['자치구']=='노원구'].copy()
    
    print(local_data.info())  # 143 행
    
    print(local_data.isnull().sum()) # 거치대수(LCD), 거치대수(QR)    
    
    '''
    
    이 부분 부터 코드 작성
    1) 결측치를 0으로 채움
    2) 2개의 컬럼값을 더하여 '거치대수' 생성    
    
    '''
    
    
    return local_data
    
def main():
    """ Main entry point of the app """
    
    data_set = load_dataset('./week4/data/공공자전거 대여소 정보(23.12월 기준).csv')
    
    #print(data_set)
    
    data_set.to_csv('./week4/data/공공자전거 대여소 정보(23.12월 기준)_노원구.csv')
    
    print('Have a good day !')
    
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
    