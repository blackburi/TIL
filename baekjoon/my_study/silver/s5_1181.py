n = int(input())
word = []

for i in range(n):
    word.append(input())
set_word = set(word)	## set으로 변환해서 중복값을 제거
word = list(set_word)	## 다시 list로 변환
word.sort()
word.sort(key = len) # sort를 len기준으로 함

for i in word:
    print(i)