question_ans = [
    {
        "question":
            '''What is Our National Bird?
A. Pigeon       B. Ostrich
C. Peacock      D. Crow''',
        "answer": "C"
    },
    {
        "question":
            '''What is Our National Bird?
A. Pigeon       B. Ostrich
C. Peacock      D. Crow''',
        "answer": "C"
    },
    {
        "question":
            '''What is Our National Bird?
A. Pigeon       B. Ostrich
C. Peacock      D. Crow''',
        "answer": "C"
    },
    {
        "question":
            '''What is Our National Bird?
A. Pigeon       B. Ostrich
C. Peacock      D. Crow''',
        "answer": "C"
    },
    {
        "question":
            '''What is Our National Bird?
A. Pigeon       B. Ostrich
C. Peacock      D. Crow''',
        "answer": "C"
    }
]
list_amount = [1000, 2000, 3000, 5000, 10000]
amount = 0
count = 0
for i in question_ans:
    print(i['question'])
    ans = input("Please write down your option: ")
    if ans == 'quit':
        amount = list_amount[count-1]
        print("You chose the quit option")
        break
    if ans == i['answer']:
        amount = list_amount[count]
        print("Sahi Jabab, Ap jit geye RS/- ", amount)
    else:
        print("galat jabab")
        break
    count += 1

print(f"Apke jite huye rakam {amount}")
