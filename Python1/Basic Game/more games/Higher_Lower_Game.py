import art
import random
import game_data

print(art.logo)


def object_picker():
    return random.choice(game_data.data)


def display(account):
    name = account['name']
    profession = account['description']
    country = account['country']
    return f"{name} ,a {profession} ,from {country}"


def answer_checker(answer, a_followers, b_followers):
    if a_followers > b_followers and answer == "a":
        return 1
    if a_followers > b_followers and answer == 'b':
        return 0
    if a_followers < b_followers and answer == 'b':
        return 1
    if a_followers < b_followers and answer == 'a':
        return 0


def game():
    score = 0
    should_continue = True
    b_account = object_picker()
    while should_continue:
        a_account = b_account
        b_account = object_picker()
        while a_account == b_account:
            b_account = object_picker()
        a_followers_count = a_account['follower_count']
        b_followers_count = b_account['follower_count']

        print(f"Compare A: {display(a_account)}.")
        print(art.vs)
        print(f"Against B: {display(b_account)}.")
        answer = input("Which has more followers A or B:").lower()

        if answer_checker(answer, a_followers_count, b_followers_count) == 1:
            score = score + 1
            print("You are right! your score", score)
        else:
            print("Game Over! Wrong answer")
            should_continue = False
    print("Your Score:", score)


game()
