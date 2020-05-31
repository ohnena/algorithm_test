

# 해답이 더 깔끔해서...
changes = 1000 - int(input())
count = 0

for i in [500, 100, 50, 10, 5, 1]:
    count += changes // i
    changes %= i

print(count)


# 당연합격..
N = 1000-int(input())


def cal_change(change):
    # coins = [500, 100, 50, 10, 5, 1]
    total = 0
    #
    # for i in range(len(coins)):
    #     a = change // coins[i]
    #     total += a
    #     change -= a * coins[i]
    return total

print(cal_change(N))