n = int(input()) # 출석 번호를 부른 횟수
a = list(map(int, input().split()))
student = [0] * 23 # 학생 번호 데이터 목록
for i in a :
    student[i-1] = a.count(i) # 부른 횟수
print(' '.join(str(i) for i in student))