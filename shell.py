import random

quit_commands = {'q!', 'Q!', 'quit', 'QUIT'}


def pick_random_numbers(n, k):
    if k > n:
        return "Error: k must be less than or equal to n"

    numbers = list(range(1, n + 1))
    random_numbers = random.sample(numbers, k)
    return random_numbers


class Shell:
    def __init__(self, content_box):
        self.path = 'Home'
        self.prompt = f'[${self.path}/]>> '
        self.content_box = content_box
        self.content_type = None

    def execute(self, command):
        command = command.split(' ')

        if command[0] == 'cd':
            self.chdir(command)
        elif command[0] == 'ls':
            self.list_dir(command)
        elif command[0] in {'quiz', 'qz'}:
            self.quiz(command)

    def chdir(self, command_list):
        path = command_list[1]

        if path == '../':
            self.path = 'Home'
            self.prompt = f'[${self.path}/]>> '
            self.content_type = None
        elif path.isnumeric():
            index = int(path)
            if not 1 <= index <= len(self.content_box):
                return

            self.content_type = list(self.content_box.keys())[index-1].split('.')[0]
            self.path = f'Home/{self.content_type}'
            self.prompt = f'[${self.path}/]>> '

    def list_dir(self, command_list):
        def print_box(num, box):
            question = box[0]
            answers = box[1::]
            print('______________________')
            print(f'{num}.')
            print(f'질문:', question)
            if len(answers) == 1:
                print('답변:', answers[0])
            else:
                print('답변:')
                for answer in answers:
                    print(f'- {answer}')
            print()

        if self.content_type:
            if len(command_list) == 1:
                for num, box in enumerate(self.content_box[self.content_type], start=1):
                    print_box(num, box)
            elif len(command_list) == 2 and command_list[1].isnumeric():
                begin = int(command_list[1]) * 10 - 1
                end = begin + 10
                for num, box in enumerate(self.content_box[self.content_type], start=1):
                    if begin <= num <= end:
                        print_box(num, box)
        else:
            for num, content_type in enumerate(self.content_box.keys(), start=1):
                print(f'{num}. {content_type}')

    def quiz(self, command):
        def pick_random(n, k):
            if k > n:
                return "Error: k must be less than or equal to n"

            numbers = list(range(0, n))
            random_numbers = random.sample(numbers, k)
            return random_numbers

        try:
            size = int(command[1])
            quiz_box = []

            if self.content_type:
                for problem in self.content_box[self.content_type]:
                    question = problem[0]
                    answer = '\n'.join([f'- {a}' for a in problem[1::]])
                    quiz_box.append([question, answer])
            else:
                for box in self.content_box.values():
                    for problem in box:
                        question = problem[0]
                        answer = '\n'.join([f'- {a}' for a in problem[1::]])
                        quiz_box.append([question, answer])

            for pick in pick_random(len(quiz_box), size):
                question, answer = quiz_box[pick]
                c = input(question)

                if c in quit_commands:
                    break
                print(answer)
                print()
        except:
            pass


# pyinstaller --add-data "BudgetTree.json;." --add-data "Transactions.xlsx;." --icon=icon_financetree.ico -n FinanceTreeApp2 main.py
