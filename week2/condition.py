import os

# 'C:\Users\sovoz' 경로에 'test' 폴더가 존재하는지 확인
directory_path = r'C:\Users\sovoz\test'

if not os.path.exists(directory_path):
    # 사용자로부터 새로운 디렉토리 이름 입력받기
    new_directory = input("새로운 디렉토리 이름을 입력하세요: ")
    
    # 새로운 디렉토리 생성
    new_directory_path = os.path.join(r'C:\Users\sovoz', new_directory)
    os.makedirs(new_directory_path)
    print(f"'{new_directory}' 디렉토리가 생성되었습니다.")
else:
    print("'test' 디렉토리가 이미 존재합니다.")