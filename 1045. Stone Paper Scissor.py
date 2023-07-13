import random


def check(comp, user):
    if comp == user:
        return 0

    if (comp == 0 and user == 1):
        return -1

    if (comp == 1 and user == 2):
        return -1

    if (comp == 2 and user == 0):
        return -1

    return 1


totalscore = 0
print("Enter 3 to exit")

while True:
    user = int(input("0 for Stone, 1 for Paper and 2 for Scissor:\n"))

    if user == 3:
        print(f"Total Score: {totalscore}")
        break

    comp = random.randint(0, 2)

    print(f"Computer's choice: {comp}")

    score = check(comp, user)

    if (score == 0):
        print("Its a draw")
    elif (score == -1):
        print("You Win")
        totalscore += 1


    else:
        print("You Lose")
        if totalscore != 0:
            totalscore -= 1
