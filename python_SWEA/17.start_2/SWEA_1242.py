# 암호의 길이가 늘어나지 않았을때(56자리 일 때)
main_dic = {
    1011000 : 0,
    1001100 : 1,
    1100100 : 2,
    1011110 : 3,
    1100010 : 4,
    1000110 : 5,
    1111010 : 6,
    1101110 : 7,
    1110110 : 8,
    1101000 : 9
}

# 암호의 길이가 늘어났을 때(56의 배수 일 때)
sub_dic = {}

# 9까지만 하는 이유는 가로 길이의 최대가 500이기 때문에
# 암호의 길이는 최대 9배까지 늘어날 수 있기 때문이다.
# 500/56=8.92... 이기 때문에 안전하게 9까지 생각
for i in range(1, 10) :
    for key in main_dic :


T = int(input())

for tc in range(1, T+1) :
    n, m = map(int, input().split())

    # 암호가 들어있는 줄만 추출, 겹치는 부분 삭제
    code = []
    for i in range(n) :
        sub = list(map(str, input()))
        if (sub != ['0'] * m) and (sub not in code) :
            code.append(sub)
    
    for i in code :
        i.reverse()

"""
decryption = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9
}

ch_len = {}

for i in range(1, 36):
    tmp = set()
    for key in decryption:
        tmp_str = ''
        for letter in key:
            tmp_str += letter * i
        tmp.add(tmp_str)
    ch_len[i] = tmp

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    codes = set()
    ch = set()
    for _ in range(N):
        S = input().strip().strip('0')
        if S and S not in ch:
            ch.add(S)
            S = bin(int(S, 16))[2:].rstrip('0')
            while S:
                for i in range(1, 36):
                    if S[-7*i:] in ch_len[i]:
                        break
                codes.add((S[-56*i:].strip('0'), i))
                S = S[:-56*i].rstrip('0')

    total = 0
    for code, cnt in codes:
        code = code.zfill(cnt * 56)
        length = len(code)
        tmp1, tmp2 = 0, 0
        for i in range(0, length, 7*cnt):
            if i//cnt % 2 == 0:
                tmp1 += decryption[code[i:i+7*cnt:cnt]]
            else:
                tmp2 += decryption[code[i:i+7*cnt:cnt]]

        if (tmp1 * 3 + tmp2) % 10 == 0:
            total += tmp1 + tmp2

    print(f"#{test_case} {total}")
"""