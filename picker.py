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

prob = [] # 숫자 각각 뽑힐 수 있는 상대적 확률
x = 20 # 확률 기본값 (모든 숫자 상대적 수치의 최솟값)

for i in times:
    prob.append(max(times) - i + x)

def list_clone(l):
    c=[]
    for i in range(len(l)):
        c.append(l[i])
    return c

def pick(repeat:int,pick:int,initprob:list,f:int,l:int)->list:
    result = []
    for j in range(0,repeat):
        result.append([0]*(l-f+1))
        probablity = list_clone(initprob)
        for i in range(0,pick):
            num = random.choices(range(f, l+1), weights=probablity)[0]
            result[-1][num-1] += 1
            probablity[num-1] = 0
    return result

result = pick(10**4, 5, prob, first, last)
counting = [0]*(last-first+1)

for i in result:
    for j in range(len(i)):
        counting[j] += i[j]

print(counting)