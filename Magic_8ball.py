import random


question = 1
messages = ['Yes', 'No', 'I dont know, try again later',
            'Hmm, something went wrong. Try asking again',
            'Yes, but but be careful','No, absolutely not!',
            'It is certain','It is decidedly so','Very doubtful']


while question != 0:

    number = random.randint(1, 9)
    question = input('What is your question?\n')
    print(messages[random.randint(0, len(messages) - 1)])



















