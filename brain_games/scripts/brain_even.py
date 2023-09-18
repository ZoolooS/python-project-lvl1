import random
import prompt

# from brain_games.scripts.brain_games import main
# from brain_games import main
from brain_games.cli import welcome_user


def is_even(num):
    return not (num % 2)


def brain_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    answers = ('no', 'yes')
    right_answers = 3
    RANGE_START = 0
    RANGE_END = 100

    while right_answers > 0:
        q_num = random.randint(RANGE_START, RANGE_END)
        q_num_is_even = is_even(q_num)
        print(f'Question: {q_num}')
        answer = prompt.string('Your answer: ')
        if (
            (answer == answers[0] and not q_num_is_even)
            or (answer == answers[1] and q_num_is_even)
        ):
            print('Correct!')
            right_answers -= 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{answers[int(q_num_is_even)]}".')
            print(f"Let's try again, {name}!")
            break

    print(f'Congratulations, {name}!') if right_answers == 0 else brain_even(name)


# main()
def main():
    name = welcome_user()
    brain_even(name)

# if __name__ == '__main__':
#     main()
