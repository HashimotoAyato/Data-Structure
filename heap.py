import heapq
a = [6,3,7,4,0,8,6,2,1,6,10]
print(a)

# リストをヒープとして扱えるように変換
heapq.heapify(a)

# (順序関係を保ったまま)要素の追加
heapq.heappush(a,5)

print(a)

# (順序関係を保ったまま)要素の取り出し
heapq.heappop(a)

for i in range(len(a)):
    print(heapq.heappop(a))