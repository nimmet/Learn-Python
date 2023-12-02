
import json

with open("data.json") as file:
    content = file.read()

quesions = json.loads(content)


correct=0
incorrect=0
isCorrect=False
notFinished=True
answerList = []
count = 1

while notFinished:
    for quesion in quesions:
        for q in quesion[:-1]:
            print(q)

        answer= input("Enter your answer: ")
        answerList.append([answer,quesion[-1]])

        if answer == quesion[-1]:
            correct +=1
        else:
            incorrect +=1

        if correct+incorrect == len(quesions):
            notFinished = False

for a in answerList:

    print(f"{count} {' Correct Answer: ' if a[0]==a[1] else ' Incorrect Answer: '} User Answer: {a[0]}, Correct Answer: {a[1]}")
    count +=1

print(f"Score {correct}/{correct+incorrect}")