# module01: 학생들의 이름과 점수를 입력받은 뒤, 리스트에 수납하는 함수
def input_students():
    students = []
    while True:
        name = input("Enter student's name (or 'quit' to stop): ")
        if name == 'quit':
            break
        score = float(input("Enter student's score: "))
        students.append((name, score))
    return students

# module02: 학생들의 평균 점수를 계산하는 함수
def calculate_average(students):
    total_score = sum(student[1] for student in students)
    return total_score / len(students)

# module03: 특정 점수 이상의 성적을 거둔 학생과 해당 학생의 점수를 출력하는 함수
def print_students_above_threshold(students, threshold):
    print(f"Students with scores above {threshold}:")
    for student in students:
        if student[1] > threshold:
            print(f"{student[0]}: {student[1]}")

def main():
    students = input_students()
    
    if not students:
        print("No students entered.")
        return

    average_score = calculate_average(students)
    print(f"Average score: {average_score}")
    
    threshold = float(input("Enter the score threshold: "))
    print_students_above_threshold(students, threshold)

if __name__ == '__main__':
    main()