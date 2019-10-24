import random

# the program will ask a user to enter in a question
# the program will respond with words of wisdom
# (randomly chosen)

ANSWERS = [
 "It is certain.",
 "It is decidedly so.",
 "Without a doubt.",
 "Yes - definitely.",
 "You may rely on it.",
 "As I see it, yes.",
 "Most likely.",
 "Outlook good.",
 "Yes.",
 "Signs point to yes.",
 "Reply hazy, try again.",
 "Ask again later.",
 "Better not tell you now.",
 "Cannot predict now.",
 "Concentrate and ask again.",
 "Don't count on it.",
 "My reply is no.",
 "My sources say no.",
 "Outlook not so good.",
 "Very doubtful.",
]


def ask_question():
    return input("Ask the wizard a question (ENTER to quit): ")


def give_response():
    return random.choice(ANSWERS)


while ask_question() != '':
    print(give_response())
