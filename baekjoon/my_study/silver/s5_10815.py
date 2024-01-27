n = int(input())
n_list = list(map(int, input().split()))

n_dict = {n_list[i] : 1 for i in range(n)}

m = int(input())
m_list = list(map(int, input().split()))

exist_list = []

for t in m_list :
    try :
        exist_list.append(n_dict[t])
    except :
        exist_list.append(0)

print(*exist_list)