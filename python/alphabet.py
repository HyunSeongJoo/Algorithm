s1 = 'aAb'
s2 = 'BA'
s3 = 'BbA'

count = [0]*26
for i in s3:
    ord_i = ord(i)
    if ord_i >= 97: # 소문자
        count[ord_i-97] += 1
    else:   # 대문자
        count[ord_i-65] += 1

res_list = [i for i, value in enumerate(count) if value == max(count)]
answer = ''
for i in res_list:
    answer += chr(i+97)
print(answer)
