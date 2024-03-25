import sys

input = sys.stdin.readline

n,m = map(int,input().split())

#a랑 b랑 합쳐도 되고, a랑 c랑 합쳐도 될 때, 각 경우의 수에 대해 dfs를 돌린다
#a랑 b랑 합친 경우에 대해
#dfs를 돌릴건데, 아직 합치지 않은 것과 합쳐진 것으로 나눈다
#합치지 않은 거에서 하나씩 꺼내서, 합쳐진 것과 비교 -> 합치고 dfs 백트레킹

genes = []
for _ in range(n): #n개의 좋은 염기서열에 대해
    genes.append(input().rstrip('\n'))

genes = list(set(genes))
def dfs(idx, exclusive_genes):
    global min_gene
    if idx >= len(genes) : #더 이상 확인할 염기서열이 없으면 중단
        min_gene = min(min_gene,len(exclusive_genes))
        return

    if len(exclusive_genes) >= min_gene: #이미 최소 슈퍼염기 개수보다 크다면 중단
        return

    flag = 0
    for j in range(len(exclusive_genes)):
        ex_gene = exclusive_genes[j]
        update_gene = ''  # 구체화 시킨 결과를 담을 곳
        for i in range(m) :
            # 만약 겹칠 수 없다면 다음 ex_gene과 비교 시작
            if genes[idx][i] != '.' and ex_gene[i] != '.' and genes[idx][i] != ex_gene[i] :
                break
            # gene이 .이 아니라면 ex_gene을 구체화한다
            elif genes[idx][i] != '.' :
                update_gene += genes[idx][i]
            else:
                update_gene += ex_gene[i]
        else: #만약 합칠 수 있다면
            flag = 1
            exclusive_genes[j] = update_gene #합친 서열로 변경
            dfs(idx+1,exclusive_genes)
            exclusive_genes[j] = ex_gene  #합치기 전으로 돌린다
    if not flag: #합칠 수 있는 ex_gene이 없다면
        exclusive_genes.append(genes[idx])
        dfs(idx+1,exclusive_genes)
        exclusive_genes.pop()

min_gene = sys.maxsize

for _ in range(len(genes)):
    exclusive_genes = []
    genes.append(genes.pop(0))
    dfs(0,exclusive_genes)

print(min_gene)