import random

first = 1 # 수 범위 설정
last = 10

response = [] # 사용자 응답
times = [0] * (last-first+1) #숫자당 나온 횟수

#응답 받기 --------------------------
working = True

while working:
    for i in range(first, last+1):
        r = (input(f"number {i} : "))
        if r == "":
            working = False
            break
        elif int(r) < first or int(r) > last:
            working = False
            break
        else:
            response.append(int(r))
            times[int(r)-1] += 1

# 확률변수 설정 ----------------------
prob = [] # 숫자 각각 뽑힐 수 있는 상대적 확률
x = 20 # 확률 기본값 (모든 숫자 상대적 수치의 최솟값)

for i in times: # 상대적 확률 설정
    prob.append(max(times) - i + x)

def list_clone(l): # 리스트 복제 : initprob 바뀌는것 방지
    c=[]
    for i in range(len(l)):
        c.append(l[i])
    return c

def pick(repeat:int,pick:int,initprob:list,numrange:tuple)->list: # 뽑기 (뽑는 횟수, 한번에 뽑는 수, 상대적 확률, 뽑기 범위)
    result = []
    f = numrange[0]
    l = numrange[1]
    for j in range(0,repeat): # repeat 번 뽑기
        result.append([0]*len(numrange)) # result 에 새로운 군 추가
        probablity = list_clone(initprob) # 확률 초기화
        for i in range(0,pick): # pick개의 수 뽑기
            num = random.choices(range(f, l+1), weights=probablity)[0]
            result[-1][num-1] += 1 # 군에 뽑힌 수 추가
            probablity[num-1] = 0 # 한 군에서 여러개의 같은 수가 나오지 않게 확률을 0으로 설정
    return result # 뽑힌 군들 반환

result = pick(10**4, 5, prob, first, last)
counting = [0]*(last-first+1)

for i in result: # 수가 뽑힌 횟수를 각각 계산
    for j in range(len(i)):
        counting[j] += i[j]

print(counting)