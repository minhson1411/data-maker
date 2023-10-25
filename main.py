import os
import random
from datetime import datetime, timedelta

def make_commit(days: int):
    if days < 1:
        return os.system("git push")
    else:
        # Sinh ngày ngẫu nhiên từ 1 đến 4
        random_days = random.choice([1, 2, 2, 3, 4])
        dates = f'{random_days} days ago'

        with open('data.txt', 'a') as file:
            file.write(f'{dates}\n')

        # Staging
        os.system('git add data.txt')
        # Commit
        os.system('git commit --date="'+dates+'" -m "commit on {dates}"')

        # Chọn cách nhau giữa các commit (chủ yếu là 2 ngày, cùng lắm là 4 ngày)
        spacing_days = random.choice([2, 2, 4])
        
        # Sử dụng đệ quy để thực hiện commit ở ngày tiếp theo
        return days * make_commit(days - spacing_days)

make_commit(700)
