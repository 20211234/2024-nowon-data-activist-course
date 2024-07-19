# 모든 오류 발생시, except 코드 실행
try:
     1 + a
except:
    print("불특정 오류가 발생했습니다.")


# 특정 오류 발생시, except 코드 실행
try:
     1 + a
except NameError:
     print("이름 오류가 발생했습니다.")


# 특정 오류 발생시, 오류 내용을 담은 오류 변수 e를 출력하는 except 코드 실행
try:
     4 / 0
except ZeroDivisionError as e:
     print(e)


# 특정 오류 발생시, 통과시키는 except 코드 실행
try:
     f = open("Untitled", 'r')
except FileNotFoundError:
     pass


# 특정 오류 여러 개 발생시, 각 오류에 해당하는 except 코드 실행
try:
     a = [1, 2]
     print(a[3])
     4/0
except ZeroDivisionError:
     print("0으로 나눌 수 없습니다.")
except IndexError:
     print("존재하지 않는 인덱스입니다.")


# 특정 오류 여러 개 발생시, 동일한 except 코드 실행
try:
     a = [1, 2]
     print(a[3])
     4/0
except (ZeroDivisionError, IndexError) as e:
     print(e)