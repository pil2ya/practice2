import random

choices = ["가위", "바위", "보"]

print("=== 가위바위보 게임 ===")

while True:
    user = input("가위, 바위, 보 중 하나를 입력하세요 (종료: q): ")

    if user == "q":
        print("게임을 종료합니다.")
        break

    if user not in choices:
        print("잘못된 입력입니다.\n")
        continue

    computer = random.choice(choices)

    print(f"\n사용자 : {user}")
    print(f"컴퓨터 : {computer}")

    if user == computer:
        print("무승부!")
    elif (
        (user == "가위" and computer == "보") or
        (user == "바위" and computer == "가위") or
        (user == "보" and computer == "바위")
    ):
        print("사용자 승리!")
    else:
        print("컴퓨터 승리!")

    print()