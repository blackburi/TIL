n = int(input())
a_set = set(map(str, input().split()))

m = int(input())
m_list = list(map(str, input().split()))

for i in m_list :
    if i in a_set :
        print(1)
    else :
        print(0)