# import libraries
import art
import textblob
import pyttsx3

# starts voice engine
engine = pyttsx3.init()

# prints header
print(art.text2art('Ministry of Work'))
print(art.art('happy'))

# define failed_to_comply function


def failed_to_comply():
    print(
        'You failed to comply with the rules of the Ministry of Work and is now being terminated.')
    engine.say(
        'You failed to comply with the rules of the Ministry of Work and is now being terminated')
    engine.runAndWait()
    print(art.text2art('ZAAAAP!'))
    engine.say('ZAAAAP!')
    engine.runAndWait()
    print(art.text2art('You Have Been Terminated!'))
    engine.say('You Have Been Terminated!')
    engine.runAndWait()
    print(art.text2art('Have a Good Day!'))
    engine.say('Have a good day!')
    engine.runAndWait()


def check_polarity(polarity):
    if polarity < 0.3:
        print(art.art('cry'))
        print('This is definetly not a positive feedback, worker. Try again!')
        engine.say(
            'This is definetly not a positive feedback, worker. Try again!')
        engine.runAndWait()
        return 'negative'
    elif polarity < 0.7:
        print(art.art('cry'))
        print('This is not a positive feedback, worker. Try again!')
        engine.say(
            'This is not a positive feedback, worker. Try again!')
        engine.runAndWait()
        return 'neutral'
    else:
        print(art.art('happy'))
        print('This is a very positive statement, worker. Keep this attitude!')
        engine.say(
            'This is a very positive statement, worker. Keep this attitude!')
        engine.runAndWait()
        return 'positive'


# counts how many times the worker inserted a blank name
blank_name = 0

# counts how many negative insights the worker provided
negative_insight = 0

# loop asking for workers name. It checks if the name is blank
# and if it is, starts countdown to termination
while True:
    print('Hello Worker. Please enter your name!')
    engine.say('Hello Worker. Please enter your name!')
    engine.runAndWait()
    name = input('> ')

    if not name:
        if blank_name <= 1:
            print('The Ministry of Work needs you to specify your name.')
            engine.say('The Ministry of Work needs you to specify your name.')
            engine.runAndWait()
            print(art.art('cofused3'))
            blank_name += 1
            continue
        elif blank_name == 2:
            print(art.art('angry'))
            print('The Ministry of Work needs you to specify your name. If you fail to comply you will be terminated.')
            engine.say(
                'The Ministry of Work needs you to specify your name. If you fail to comply you will be terminated.')
            engine.runAndWait()
            blank_name += 1
            continue
        else:
            failed_to_comply()
            exit()
    break

# loop to ask worker for an insight about its workday
while True:

    if negative_insight >= 3:
        failed_to_comply()
        exit()

    print(f'Hello employee {name}. We hope you had a great work day today!')
    engine.say(
        (f'Hello employee {name}. We hope you had a great work day today!'))
    engine.runAndWait()

    print('Please enter your positive statement about the Ministry of Work.')
    engine.say('Please enter your positive statement about the Ministry of Work.')
    engine.runAndWait()
    statement = textblob.TextBlob(input('> '))

    feedback = check_polarity(statement.sentiment.polarity)

    if feedback == 'negative':
        negative_insight += 1
        continue
    elif feedback == 'neutral':
        continue
    else:
        break

print(f'We appreciate your feedback, {name}. Have a good day!')
engine.say(f'We appreciate your feedback, {name}. Have a good day!')
engine.runAndWait()
