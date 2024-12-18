import random

first = 1
last = 10

times = []
prob = []
response = []
r = 0

for i in range(first, last+1):
    times.append(0)

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

x = 20

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