# 암호 만들기

import sys
input = sys.stdin.readline


# 모음, 자음의 개수를 체크하는 함수
def check() :
    vowel, consonant = 0, 0
    for i in answer :
        if i in vowels :
            vowel += 1
        else :
            consonant += 1
    
    # 문제 조건 체크 -> return
    if vowel >= 1 and consonant >= 2 :
        return True
    return False


# index, 사용한 문자의 개수
def password(idx, length) :
    global l

    if length == l :
        if check() :
            print(''.join(answer))
        return
    
    for i in range(idx, c) :
        answer.append(letters[i])
        password(i+1, length+1)
        answer.pop()



l, c = map(int, input().split())
letters = list(input().rstrip().split())
letters.sort()
vowels = ['a', 'e', 'i', 'o', 'u']

# 정답이 포함될 문자열
answer = []

password(0, 0)