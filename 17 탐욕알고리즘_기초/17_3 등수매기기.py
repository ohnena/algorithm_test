
# 합격>> abs함수 사용하도록 수정해봤다...성능업!

N = int(input())

hope_rank = []
for _ in range(N):
    hope_rank.append(int(input()))
hope_rank.sort()
result = 0
for i in range(len(hope_rank)):
    # if (hope_rank[i] - (i+1)) < 0:
    #     result += (hope_rank[i] - (i+1)) * -1
    # else:
    #     result += (hope_rank[i] - (i + 1))
    result += abs(hope_rank[i] - (i + 1))
print(result,hope_rank)


