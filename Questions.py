class Question:
    def __init__(self,question):
        self.__question=question
        self.__answer=0
        self.__yes=0
        self.__no=0
    def getAnswer(self,answer):
        if answer.lower()=='yes' or answer.lower()=='no':
            self.__answer=answer
        else:
            answer=input('please insert your answer again:')
            return self.getAnswer(answer)

    def returnQuestion(self):
        return self.__question
    def returAnswer(self):
        return self.__answer
    def increseStatistic(self,response):
        if response=='yes':
            self.__yes+=1
        elif response=='no':
            self.__no+=1
    def returnStatistic(self,response):
        if response=='yes':
            return  self.__yes
        elif response=='no':
            return  self.__no

pizza=Question('Did you like pizza?')
games=Question('Did you like games?')
movies=Question('Do you like movies?')
sport=Question('Do you enjoy doing sport?')
prolan=Question('Do you love Python?')

questionList=[pizza,games,movies,sport,prolan]
