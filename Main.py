import Questions
from Survey import Survey

while True:
    name=input('Your name: ')
    yesno=input('HI {} Do you want to take a survey?: '.format(name))
    if yesno.lower()=='yes':
        person=Survey(name)
        person.takeASurvey()
        yesno=input('Do you want to see yor answers? ')
        if yesno.lower()=='yes':
            print('-'*10)
            person.printAnswers()
        else:
            pass
        yesno=input('Do you want to save your answers? ')
        if yesno.lower()=='yes':
            person.saveAnswers()
        else:
            pass
        print('-'*10)
        anotherPerson=input('There is another person to take this survey? ')
        if anotherPerson=='yes':
            pass
        else:
            break
    else:
        break
