import heapq

N, L, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 地点と補給量を対応づけ
S = list(zip(A,B))
# 地点が近い順にアクセスできるようヒープを生成
heapq.heapify(S)

# 補給回数、初期地点、初期残量
count, l, p = 0, 0, P

# 過ぎた地点のそれぞれの補給量
past = []
heapq.heapify(past)

while l + p < L:
    # pだけ進んだことにする
    l += p
    p = 0

    # 通り過ぎたガソリンスタンドの補給量をヒープに記録(最大の要素から取り出せるように正負反転)
    while len(S) > 0 and S[0][0] <= l:
        heapq.heappush(past, heapq.heappop(S)[1] * (-1))

    # 通り過ぎたガソリンスタンドの中で補給量が最大のところで補給
    if len(past) > 0:
        p += heapq.heappop(past) * (-1)
        count += 1
        
    # 通り過ぎた、かつ、まだ補給していないガソリンスタンドない
    else:
        count = -1
        break
    
print(count)

    



