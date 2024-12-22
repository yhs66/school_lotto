# from ReadDB import ReadDB

import random

first = 1 # 수 범위 설정
last = 10

repeat = 10**5 # 뽑기 반복 횟수
picks = 5 # 뽑을 번호 개수

# dbData = ReadDB.readDB() # 사용자 응답
data = []
dbData = [['1', '2', '3', '4', '5'], ['1', '6', '7', '9', '10'], ['2', '7', '6', '3', '4'], ['1', '2', '7', '4', '10'], ['1', '7', '2', '4', '5'], ['1', '2', '3', '7', '8'], ['3', '4', '8', '7', '4'], ['8', '8', '4', '6', '5'], ['10', '4', '9', '4', '4'], ['1', '6', '7', '2', '4'], ['1', '2', '6', '8', '3'], ['1', '2', '7', '6', '8'], ['1', '6', '2', '4', '9'], ['1', '2', '7', '6', '5'], ['1', '7', '7', '8', '9'], ['2', '9', '8', '7', '1'], ['3', '7', '2', '3', '9'], ['9', '7', '1', '4', '10'], ['2', '8', '7', '1', '3'], ['1', '2', '7', '6', '8'], ['1', '2', '7', '6', '8'], ['3', '1', '7', '8', '9'], ['2', '7', '6', '1', '9'], ['2', '1', '7', '8', '3'], ['1', '2', '7', '9', '5'], ['1', '2', '7', '6', '8'], ['9', '10', '5', '3', '7'], ['2', '3', '8', '1', '6'], ['8', '2', '5', '10', '8'], ['7', '4', '2', '10', '3'], ['1', '2', '7', '9', '10'], ['2', '2', '7', '6', '1'], ['1', '2', '6', '8', '3'], ['1', '2', '8', '7', '9'], ['1', '2', '7', '6', '8'], ['1', '2', '8', '7', '4'], ['1', '2', '7', '6', '8'], ['4', '10', '3', '3', '7']]
for numbers in dbData:
    data.append(list(map(lambda n: int(n), numbers)))

times = [0] * (last-first+1) # 숫자당 나온 횟수

for numbers in data:
    for n in numbers:
        times[n - 1] += 1

# 확률변수 설정 ----------------------
prob = [] # 숫자 각각 뽑힐 수 있는 상대적 확률
x = 20 # 확률 기본값 (모든 숫자 상대적 수치의 최솟값)

for i in times: # 상대적 확률 설정
    prob.append(max(times) - i + x)

def list_clone(l:list) -> list: # 리스트 복제 : initprob 바뀌는것 방지
    c=[]
    for i in range(len(l)):
        c.append(l[i])
    return c

def pick(repeat:int,pick:int,initprob:list,numrange:tuple)->list: # 뽑기 (뽑는 횟수, 한번에 뽑는 수, 상대적 확률, 뽑기 범위)
    result = []
    f = numrange[0]
    l = numrange[1]
    for j in range(0,repeat): # repeat 번 뽑기
        result.append([0]*(l-f+1)) # result 에 새로운 군 추가
        probablity = list_clone(initprob) # 확률 초기화
        for i in range(0,pick): # pick개의 수 뽑기
            num = random.choices(range(f, l+1), weights=probablity)[0]
            result[-1][num-1] += 1 # 군에 뽑힌 수 추가
            probablity[num-1] = 0 # 한 군에서 여러개의 같은 수가 나오지 않게 확률을 0으로 설정
    return result # 뽑힌 군들 반환

def percentage(probablity:list) -> list: # 상대적 확률을 절대적 확률로 변환
    total = sum(probablity)
    return [round(i/total,3) * 100 for i in probablity]

result = pick(repeat, picks, prob, (first, last))

counting = [0]*(last-first+1) # 수가 뽑힌 각각의 횟수
for i in result:
    for j in range(len(i)):
        counting[j] += i[j]

print(f"\nTimes number inputed : {times}\n"+
f"Times number picked : {counting}\n"+
f"Statistical probablity : {percentage(counting)}\n\n")