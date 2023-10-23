import os
from random import randint

for i in range(0,6):
    for j in range(20):
        f = randint(1,30)
        for k in range(0, randint(1, 10)):
            d=str(i*30 + f) + " days ago"
            with open('file.txt','a') as file:
                file.write(d)
            os.system('git add .')
            os.system('git commit --date="' + d + '" -m "commit"')

# for i in range(1, 30):
#     for j in range(0, randint(1, 10)):
#         d=str(i) + " days ago"
#         with open('file.txt','a') as file:
#             file.write(d)
#         os.system('git add .')
#         os.system('git commit --date="' + d + '" -m "commit"')

os.system('git push -u origin main')