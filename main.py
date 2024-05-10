from shell import Shell
from get_contents import get_content_box
import random

quit_commands = {'q!', 'Q!', 'quit', 'QUIT'}


def pick_random(n, k):
    if k > n:
        return "Error: k must be less than or equal to n"

    numbers = list(range(1, n + 1))
    random_numbers = random.sample(numbers, k)
    return random_numbers


def __main__():
    try:
        content_box = get_content_box()
        shell = Shell(content_box)

        while True:
            try:
                command = input(shell.prompt)
                if len(command):
                    if command in quit_commands:
                        break
                    else:
                        shell.execute(command)
            except:
                pass
    except Exception as e:
        print(e)


if __name__ == '__main__':
    __main__()
