import sys
sys.stdout.reconfigure(encoding='utf-8')

"""
전역변수: 함수 밖에서 선언한 함수
지역변수: 함수 안에서 선언한 함수

global: 전역변수를 사용하겠다는 의미를 가진 예약어
nonlocal: 함수 안에 또 다른 함수가 있을 때, 바깥함수의 지역변수를 사용하겠다는 의미를 가진 예약어
"""

# 전역변수 정의
total = 0

# 함수 정의
def sum(a, b):
    global total # 전역변수 total 사용 선언
    total = a + b
    print(f"두 수의 합은 {total}입니다.")

sum(10, 20) # 함수 호출
print(f"전역변수 total의 값은 {total}입니다.")

# 바깥 함수 정의
def outer_function():
    # 바깥 함수의 지역변수 정의
    count = 0

    # 안쪽 함수 정의
    def inner_function():
        nonlocal count # 바깥 함수의 지역변수 count 사용 선언
        count += 1
        print(f"inner_function이 {count}번째 호출되었습니다.")
    
    inner_function() # 안쪽 함수 호출 X 3
    inner_function()
    inner_function()
    
outer_function() # 바깥 함수 호출

"""
Python은 main 함수 필수 X! 자동으로 최상위 수준의 코드가 실행된다.
단, 실제 프로젝트를 개발할 때는 main 함수를 사용하는 것이 일반적인 관행
"""