import Questions

def makeStatistic(yes,no):
    total=yes+no
    yesPercent=yes*100/total
    noPercent=100-yesPercent
    print('Yes: {}% \nNo: {}%'.format(yesPercent,noPercent))
    print('----------------------')

file=open('Files.txt','r')
for line in file:
    fileName=line
    survey=open('Files/{}'.format(fileName[0:len(fileName)-2]),'r')
    for text in survey:
        if text.__contains__('Question') or text.__contains__('Answer'):
            for i in Questions.questionList:
                if text.__contains__(i.returnQuestion()):
                    answerLine=survey.__next__()
                    if answerLine.__contains__('Answer:'):
                        if answerLine.__contains__('yes'):
                            i.increseStatistic('yes')
                        if answerLine.__contains__('no'):
                            i.increseStatistic('no')

        else:
           pass
    survey.close()
file.close()
for i in Questions.questionList:
    print(i.returnQuestion())
    makeStatistic(i.returnStatistic('yes'),i.returnStatistic('no'))