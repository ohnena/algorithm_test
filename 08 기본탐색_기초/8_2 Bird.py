# 8.2 새
# 1568
# easy,탐색,20분

# 핵심아이디어
# -N이 최대 1,000,000,000 이지만, K가 반복적으로 증가하여, 1+2+3+...+K = N의 등차수열원리에 의해...
# O(K^2)의 시간복잡도를 갖는다. N이 10억이라고 하더라도, 10억번 연산을 할일이 없다는 뜻이다.
# -예를 들어, N=14일때,
# 게임의 과정이 1+2+3+4+1+2+1=14이다.
# 즉 7번의 루프를 돌아서 14를 완성시킨다는 얘기다.
# -그결과 O(루트N)이 시간복잡도가된다.
# -그래서 걱정말고, 단순구현으로 가도 괜찮다.


# 14
#
# 7


# 직접
def bird(number):
    sum = 0
    K = 1
    sec_count = 0
    while sum < number:
        if sum + K > number:
            K = 1
        sum += K
        K += 1
        sec_count += 1
    return sec_count

# <<< TEST CODE START >>>
N = 14
answer = 7
assert bird(N) is answer
# <<< TEST CODE END >>>

# N = int(input())
# print(bird(N))


# 해답  //sum을 굳이 사용하지 않고, bird number를 -해서 체크하기때문에, 조금더 깔끔한느낌...
def bird_(number):
    # sum = 0
    K = 1
    sec_count = 0
    while number > 0:
        if K <= number:
            # sum += K
            number -= K
            K += 1
            sec_count += 1
        else:
            K = 1
    return sec_count


# <<< TEST CODE START >>>
N = 14
answer = 7
assert bird_(N) is answer
# <<< TEST CODE END >>>

N = int(input())
print(bird_(N))