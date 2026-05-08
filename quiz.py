def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")


questions = [
    {
        "prompt": "What does 'print()' do in Python?",
        "options": [
            "A. It adds two numbers",
            "B. It saves data to a file",
            "C. It displays text or values on the screen",
            "D. It makes a new variable"
        ],
        "answer": "C"
    },
    {
        "prompt": "Which of these is a valid variable name in Python?",
        "options": [
            "A. 2name",
            "B. name_2",
            "C. name-2",
            "D. @name"
        ],
        "answer": "B"
    },
    {
        "prompt": "What is the output of: print(2 + 3 * 2)?",
        "options": [
            "A. 10",
            "B. 12",
            "C. 8",
            "D. 7"
        ],
        "answer": "C"
    },
    {
        "prompt": "Which data type is used to store True or False?",
        "options": [
            "A. int",
            "B. string",
            "C. float",
            "D. bool"
        ],
        "answer": "D"
    },
    {
        "prompt": "What is a function in Python?",
        "options": [
            "A. A type of loop",
            "B. A block of code that runs only once",
            "C. A reusable block of code that performs a task",
            "D. A built-in variable"
        ],
        "answer": "C"
    }
]

run_quiz(questions)
