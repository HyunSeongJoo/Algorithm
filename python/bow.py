import math

target1 = [2,2,2,2,2]
target2 = [2,3,4,3,2]
positions1 = [[0,0],[0,1],[1,1],[-3,5],[7,5],[10,0],[-15,22],[-6,-5],[3,3],[5,-5]]

result = 0
for x,y in positions1:
    distance = math.sqrt(x ** 2 + y ** 2)
    for i in range(target1.__sizeof__()):
        r = sum(target1[0:i+1])
        # print('r is ',r)
        if distance <= r:
            result += 10-2*i
            print(10-2*i,end=' ')
            break

print('\n',result)

result = 0
for x,y in positions1:
    distance = math.sqrt(x ** 2 + y ** 2)
    for i in range(target2.__sizeof__()):
        r = sum(target2[0:i+1])
        # print('r is ',r)
        if distance <= r:
            result += 10-2*i
            print(10-2*i,end=' ')
            break

print('\n',result)