def boyer_moore(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    skip = []

    # 휴리스틱 함수 계산
    for i in range(256):
        skip.append(pattern_length)
    for i in range(pattern_length - 1):
        skip[ord(pattern[i])] = pattern_length - i - 1

    # 검색
    i = pattern_length - 1
    while i < text_length:
        j = pattern_length - 1
        while text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += max(skip[ord(text[i])], pattern_length - j)

    return -1

text = "ABABCABABABAABCABAB"
pattern = "BAABCABAB"

result = boyer_moore(text, pattern)
if result != -1:
    print("패턴이 텍스트에서 발견되었습니다. 인덱스:", result)
else:
    print("패턴이 텍스트에 존재하지 않습니다.")