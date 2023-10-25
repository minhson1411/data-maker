import os

import random

import random

def generate_biased_integer():
    values = [1, 2, 2, 3, 4]
    return random.choices(values)[0]


def make_commit(days: int):
    if days < 1:
        return os.system("git push")
    else:
        dates = f'{days} days ago'

        with open('data.txt', 'a') as file:
            file.write(f'{dates}\n')

        #Staging
        os.system('git add data.txt')
        #Commit
        os.system('git commit --date="'+dates+'" -m "first commit"')

        return days * make_commit(days - generate_biased_integer())
make_commit(700)
