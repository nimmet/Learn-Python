import json

with open("data_dict.json") as file:
    content = file.read()

data = json.loads(content)

score = 0

for questions in data:

    print(questions["question"])
    for index,alternatives in enumerate(questions["alternatives"]):
        print(f"{index+1}.{alternatives}")

    user_answer = int(input("Enter your answer: "))
    questions["user_answer"] = user_answer
    if questions["answer"] == user_answer:
        score += 1


for index,questions in enumerate(data):

    print(f"{index+1} {' Correct Answer: ' if questions['answer']==questions['user_answer'] else ' Incorrect Answer: '} User Answer: {questions['user_answer']}, Correct Answer: {questions['answer']}")

print(f"Score: {score}/{len(data)}")
