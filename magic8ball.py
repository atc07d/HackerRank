# Magic 8-Ball
# ac 09 30 17
# 
import random

responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definetly',
             'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',
             'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later',
             'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
             'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good',
             'Very doubtful']

while True:
    print("My gentleman or gentlelady, please ask your yes-no question or type quit.")
    question = input()
    if question in "quit":
        break
    answer_num = random.randrange(20)
    answer = responses[answer_num]
    while answer_num < 25:
        print('thinking...')
        answer_num += 1
    print(answer)
    
    
    
