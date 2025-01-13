import random

def display_menu():
    """
    Display the main menu and return the user's choice.
    """
    print("\nWelcome to the Quiz Game!")
    print("1) Play the quiz")
    print("2) View and add questions")
    print("3) Exit")
    choice = input("Enter your choice (1, 2, or 3): ").strip()
    return choice


def view_and_add_questions(questions):
    """
    View existing questions and allow the user to add new ones.

    Args:
        questions (list): The current list of quiz questions.
    """
    print("\nCurrent Questions:")
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)
        print(f"Answer: {q['answer']}")

    add_new = input("\nDo you want to add a new question? (yes/no): ").strip().lower()
    if add_new in ['yes', 'y']:
        question_text = input("Enter the question text: ").strip()
        options = [
            input("Enter option A: ").strip(),
            input("Enter option B: ").strip(),
            input("Enter option C: ").strip(),
            input("Enter option D: ").strip(),
        ]
        correct_answer = input("Enter the correct answer (A, B, C, or D): ").strip().upper()

        new_question = {
            "question": question_text,
            "options": [f"A) {options[0]}", f"B) {options[1]}", f"C) {options[2]}", f"D) {options[3]}"],
            "answer": correct_answer
        }
        questions.append(new_question)
        print("\nNew question added successfully!")


def play_quiz(questions):
    """
    Play the quiz game.

    Args:
        questions (list): The list of quiz questions.
    """
    if not questions:
        print("\nNo questions available! Add some first.")
        return

    print("\nStarting the Quiz!")
    score = 0

    random.shuffle(questions)

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nQuiz Over! You scored {score}/{len(questions)}.")


def quiz_game_with_menu():
    """
    Main function to run the quiz game with a menu.
    """
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
            "answer": "A"
        },
        {
            "question": "What is 5 + 3?",
            "options": ["A) 5", "B) 8", "C) 9", "D) 7"],
            "answer": "B"
        }
    ]

    while True:
        choice = display_menu()

        if choice == '1':
            play_quiz(questions)
        elif choice == '2':
            view_and_add_questions(questions)
        elif choice == '3':
            print("\nThank you for playing! Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")


quiz_game_with_menu()
