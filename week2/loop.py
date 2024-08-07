# 세 학생의 다섯 과목 점수를 담은 배열
std1 = [39, 29, 95, 70, 49]
std2 = [60, 62, 79, 86, 29]
std3 = [10, 20, 30, 40, 50]

# 한 학생의 다섯 과목 점수 총계를 담을 변수
score1 = 0
score2 = 0
score3 = 0

# 점수 배열의 첫번째 요소부터 다섯번째 요소까지 더하는 반복문
'''
range(0, 5)의 해석: i가 5가 되는 바로 그 순간, 이어지는 연산을 수행하지 않고 즉시 탈출!
시작값: 반복횟수에 포함
끝값: 반복횟수에 미포함
'''
for i in range(0, 5):
    score1 = score1 + std1[i]
    score2 = score2 + std2[i]
    score3 = score3 + std3[i]

print("학생1의 평균 점수: {}\n학생2의 평균 점수: {}\n학생3의 평균 점수: {}".format(score1/5, score2/5, score3/5))