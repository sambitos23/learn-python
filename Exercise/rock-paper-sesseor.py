import random


def check(comp, user):
    if comp == user:
        return 0
    if comp == 0 and user == 1:
        return -1
    if comp == 1 and user == 2:
        return -1
    if comp == 2 and user == 0:
        return -1

    return 1


def check_value(value):
    if value == 0:
        return "Paper"
    elif value == 1:
        return "Rock"
    else:
        return "Scissors"


def check_score(score, point):
    if score == 0:
        point += 0
        print("\nIt's Draw")
    elif score == 1:
        point += 1
        print("\nYou Win")
    else:
        point += -1
        print("\nYou Lose")
    return point


print("You have 3 chance to win the game: ")
point = 0
for index in range(3):
    print(f"This is your {index+1} turn")
    comp = random.randint(0, 2)
    user = int(input("0 for Paper \n1 for Rock \n2 for Scissors \n"))

    score = check(comp, user)
    print("\nYou: ", check_value(user))
    print("Computer: ", check_value(comp))

    point = check_score(score, point)


if point < 0:
    print("\nSorry, You lost the game..... pls try again\nTotal point: ", point)
elif point == 0:
    print("\nSorry, It's a draw.... pls try again\nTotal point: ", point)
else:
    print("\nCongratulations, you won the game\nTotal point: ", point)
