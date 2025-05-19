
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. London", "C. Paris", "D. Madrid"],
        "answer": "C"
    },
    {
        "question": "Which language is used to create Android apps?",
        "options": ["A. Java", "B. Python", "C. C++", "D. Swift"],
        "answer": "A"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Bjarne Stroustrup"],
        "answer": "C"
    }
]

def run_quiz():
    score = 0
    for idx, q in enumerate(questions):
        print(f"\nQuestion {idx + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}")

    print("\nQuiz completed!")
    print(f"Your final score is {score} out of {len(questions)}")

if __name__ == "__main__":
    run_quiz()


