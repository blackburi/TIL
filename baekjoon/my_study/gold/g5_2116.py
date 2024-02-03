N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
new_len = []  # 0~5 인덱스 시작을 기준으로 주사위의 옆면 최고치 합을 모아 놓을 리스트 선언

for i in range(6):  # 주사위 하나의 길이 만큼 돈다.
    start = i  # 시작 값의 인덱스를 start라는 변수에 대입
    result = 0  # 결과값을 0으로 초기화
    for j in range(len(dice)):  # 입력받은 주사위의 길이만큼 돈다.

        if start == 0 or start == 5:  # 만약 주사위의 인덱스가 0 이나 5라면
            result += max(dice[j][1:5])  # 0, 5번을 제외한 나머지 주사위 면중 가장 큰 값을 더해준다
            if j != len(dice) - 1 and start == 0:  # 만약 인덱스가 마지막이 아니고 0이 라면
                start = dice[j + 1].index(dice[j][5])  # 다음 인덱스 값을 현재5번째 인덱스가 존재하는 값을 다음 주사위에서 찾아서 대입
            elif j != len(dice) - 1 and start == 5:  # 만약 인덱스가 마지막이 아니고 5 라면
                start = dice[j + 1].index(dice[j][0])  # 다음 인덱스 값을 현재0번째 인덱스가 존재하는 값을 다음 주사위에서 찾아서 대입

        elif start == 2 or start == 4:  # 만약 주사위의 인덱스가 2 이나 4라면
            result += max(dice[j][0:2] + [dice[j][3]] + [dice[j][5]])  # 2, 4번을 제외한 나머지 주사위 면중 가장 큰 값을 더해준다
            if j != len(dice) - 1 and start == 2:  # 만약 인덱스가 마지막이 아니고 2이 라면
                start = dice[j + 1].index(dice[j][4])  # 다음 인덱스 값을 현재4번째 인덱스가 존재하는 값을 다음 주사위에서 찾아서 대입
            elif j != len(dice) - 1 and start == 4:  # 만약 인덱스가 마지막이 아니고 4 라면
                start = dice[j + 1].index(dice[j][2])  # 다음 인덱스 값을 현재2번째 인덱스가 존재하는 값을 다음 주사위에서 찾아서 대입

        elif start == 1 or start == 3:  # 만약 주사위의 인덱스가 1 이나 3라면
            result += max([dice[j][0]] + [dice[j][2]] + dice[j][4:])  # 1, 3번을 제외한 나머지 주사위 면중 가장 큰 값을 더해준다
            if j != len(dice) - 1 and start == 1:  # 만약 인덱스가 마지막이 아니고 1이 라면
                start = dice[j + 1].index(dice[j][3])  # 다음 인덱스 값을 현재3번째 인덱스가 존재하는 값을 다음 주사위에서 찾아서 대입
            elif j != len(dice) - 1 and start == 3:  # 만약 인덱스가 마지막이 아니고 3이 라면
                start = dice[j + 1].index(dice[j][1])  # 다음 인덱스 값을 현재1번째 인덱스가 존재하는 값을 다음 주사위에서 찾아서 대입
    new_len.append(result) # N개의 주사위를 다 돈 N개의 옆면 합을 대입한다.

print(max(new_len)) # 그중 가장 큰 값을 출력