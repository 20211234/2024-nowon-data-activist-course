import pandas as pd
from geopy.geocoders import Nominatim
from tqdm import tqdm
from geopy.exc import GeocoderTimedOut

geo_local = Nominatim(user_agent='South Korea', timeout=500)

# 위도, 경도 반환하는 함수
def geocoding(address, attempt=1, max_attempts=5):
    try:
        geo = geo_local.geocode(address)
        x_y = [geo.latitude, geo.longitude]
        return x_y
    except GeocoderTimedOut:
        if attempt <= max_attempts:
            return geocoding(address, attempt=attempt+1)
        raise
    except:
        return [0,0]
    
# 변환할 주소    
csv = pd.read_csv('./week5/data/cafe.csv')
print(csv.head())

# 데이터프레임 주소값 추출
address= csv['소재지도로명주소']
print(address.head())

# 상세주소 분리
for i in range(len(address)):
    a = address[i].split(' ')
    address[i] = " ".join(a[0:4])
print(address)

latitude = []
longitude =[]

for i in tqdm(address):                 # 진행율 표시
    latitude.append(geocoding(i)[0])
    longitude.append(geocoding(i)[1])
    
# 필요한 항목 정리    
address_df = pd.DataFrame({'카페이름': csv['사업장명'],'상세주소':csv['소재지도로명주소'],'주소':address,'위도':latitude,'경도':longitude})

#df저장
#address_df.to_csv('cafe_20220812_ex.csv', encoding='utf-8') # utf-8-sig
address_df.to_csv('./week5/data/cafe.csv', index_label='No', encoding='utf-8')