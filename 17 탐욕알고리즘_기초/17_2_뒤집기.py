

# 해답 >> 변수를 최소로 사용한듯!....인상적인 코드다...
data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))

# 합격 >> 다만 변수가 4개나 쓰였다...해답에선 3개네...
exit()
s = input()

zero = 0
one = 0

tip = ''
for  c in s:
    if tip == '':
        tip = c
        if tip == '0':
            zero += 1
        else:
            one += 1
        continue

    if tip != c:
        tip = c
        if tip == '0':
            zero += 1
        else:
            one += 1

print(min(zero, one))


