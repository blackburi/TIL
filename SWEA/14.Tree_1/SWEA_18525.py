T = int(input())

for tc in range(1, T+1) :
    n = int(input())

    lst = [0]
    def inorder(x) :
        if x > n :
            return
        if x :
            inorder(2*x)
            lst.append(x)
            inorder(2*x+1)

    # ans[a] = b : a번째 노드에는 b가 들어있다.
    inorder(1)
    print(lst)