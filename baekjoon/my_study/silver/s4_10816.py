import sys

input = sys.stdin.readline

n = int(input())
n_lst = list(map(int, input().split()))

m = int(input())
m_lst = list(map(int, input().split()))

m_dic = {}

for i in range(m) :
    m_dic[m_lst[i]] = 0


for j in n_lst :
    if j in m_dic :
        m_dic[j] += 1

ans = []
for k in m_lst :
    ans.append(m_dic[k])

print(*ans)