import Questions

class Survey:
    def __init__(self,personName):
        self.__personName=personName
        self.__questionList=Questions.questionList
    def takeASurvey(self):
        for i in(self.__questionList):
            print(i.returnQuestion())
            i.getAnswer(input('Answer: '))

    def printAnswers(self):
        for i in self.__questionList:
            print(i.returnQuestion())
            print(i.returAnswer())

    def saveAnswers(self):
        try:
            savedFiles=open('Files.txt','a')
            savedFiles.write('{}.txt \n'.format(self.__personName))
            savedFiles.close()
            file=open('Files/{}.txt'.format(self.__personName),'w')
            for i in self.__questionList:
                 file.write('Question: '+i.returnQuestion()+'\nAnswer: '+i.returAnswer()+'\n')
            file.close()
        except:
            print('Error')
