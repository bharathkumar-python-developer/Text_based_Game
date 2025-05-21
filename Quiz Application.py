import random

# Quiz data
questions = [
    {"question": "What is the capital of France?", "answers": ["Paris", "London", "Berlin"], "correct": 0},
    {"question": "What is the largest planet in our solar system?", "answers": ["Earth", "Saturn", "Jupiter"], "correct": 2},
    {"question": "Who painted the Mona Lisa?", "answers": ["Leonardo da Vinci", "Michelangelo", "Raphael"], "correct": 0},
    {"question": "What is the chemical symbol for gold?", "answers": ["Ag", "Au", "Hg"], "correct": 1},
    {"question": "Which language is spoken in Brazil?", "answers": ["Spanish", "Portuguese", "French"], "correct": 1}
]

def quiz():
    score = 0
    random_questions = random.sample(questions, len(questions))  # Randomize question order
    
    for question in random_questions:
        print(question["question"])
        for i, answer in enumerate(question["answers"]):
            print(f"{i+1}. {answer}")
        
        while True:
            try:
                user_answer = int(input("Enter your answer: ")) - 1
                if 0 <= user_answer < len(question["answers"]):
                    break
                else:
                    print("Invalid answer. Please enter a number corresponding to an answer.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        if user_answer == question["correct"]:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer was {question['answers'][question['correct']]}")
    
    print(f"Your score is {score}/{len(questions)}")
    
    # Ask user if they want to play again
    play_again = input("Would you like to play again? (yes/no): ")
    if play_again.lower() == "yes":
        quiz()
    else:
        print("Thanks for playing!")

quiz()
