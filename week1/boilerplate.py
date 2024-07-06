# 한 줄 주석

'''
여러 줄 주석
인터프리터는 우리가 작성한 코드를 기계어로 번역할 때 주석 영역을 건너뛴다!
'''

__author__ = "장은선"
__version__ = "0.1.0"
__license__ = "덕성여자대학교"

# sum 함수 정의
def sum(a, b):
    return a + b

# main 함수 정의
def main():
    """ Main entry point of the app """
    print("Hello World!")
    result = sum(3, 4)
    print(result)

# 선언한 main 함수 호출
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

'''
__name__: Python에서 현재 실행 중인 모듈의 이름을 나타내는 내장 변수
모듈: 함수나 변수 또는 클래스를 모아 둔 Python 파일
내장변수(=빌트인변수): Python에 미리 만들어져 있는 특별한 변수
위 조건문의 의미: 현재 실행 중인 모듈의 이름이 main이라면, 아래 코드를 실행하라는 뜻
'''