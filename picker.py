# from ReadDB import ReadDB

import random

first = 1 # 수 범위 설정
last = 11 # picks 보다 커야함함

x = 10 # 확률 기본값 (모든 숫자 상대적 수치의 최솟값)

repeat = 100**2 # 사람 수
picks = 5 # 뽑을 번호 개수



# 확률변수 설정 ----------------------




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

# dbData = ReadDB.readDB()
data = []
dbData = pick(repeat,5,[1]*10,(1,10))
for numbers in dbData:
    data.append(list(map(lambda n: int(n), numbers)))

times = [0] * (last-first+1) # 숫자당 나온 횟수
prob = [] # 숫자 각각 뽑힐 수 있는 상대적 확률률

for numbers in data:
    for n in numbers:
        times[n - 1] += 1

for i in times: # 상대적 확률 설정
    prob.append(max(times) - i + x)

result = pick(1, picks, prob, (first, last))
response = pick(repeat, picks, [1]*(last-first+1), (first,last))

matches = [0] * len(response)
winners = [0] * (picks+1)

for p in range(len(response)):
    for i in range(len(response[p])):
        if response[p][i] == result[0][i] and response[p][i] == 1:
            matches[p] += 1
    winners[matches[p]] += 1

print(winners)
for i in range(len(winners)):
    print(f'{picks-i+1}등 : {percentage(winners)[i]} (300명중 {round(3*percentage(winners)[i])}명 꼴)')