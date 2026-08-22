import sys

def ask_question(question, correct_answer, correct_message, incorrect_message): # Handles questions with unlimited attempts
    while True:    
        print(question)
        answer = input().strip()
        
        if answer == correct_answer:
            print(correct_message)
            break
        else:
            print(incorrect_message)

def one_attempt(question, correct_answer, correct_message, incorrect_message):# Handles questions with 1 attempt
    print(question)
    answer = input().strip()
    
    if answer == correct_answer:
        print(correct_message)
        return True
    else:
        print(incorrect_message)
        return False

ask_question(
    "What is 5 x 5?",
    "25",
    "Easy, next one.",
    "Try again."
)

ask_question(
    "10 + x = 15. What is x?",
    "5",
    "Still easy, let's keep going.",
    "C'mon, this is easy!"
)

ask_question(
    "What is the square root of 81?",
    "9",
    "This is just the start...",
    "This is year 5 stuff, try again."
)

ask_question(
    "What is the area of a circle if its radius is 6? Leave your answer in terms of pi. NOTE: just write the integer",
    "36",
    "Think you're smart huh..",
    "Think harder."
)

ask_question(
    "What is the density of my cube if the mass is 50kg and the volume is 100 metres cubed?",
    "0.5",
    "Getting harder huh. Keep going.",
    "HAHA! I bet he doesn't know the formula is Density = Mass ÷ Volume... forget I said that."
)

if not one_attempt(
    "I have a right-angled triangle with sides of 3 cm and 4 cm. What is the length of the hypotenuse?",
    "5",
    "IMPOSSIBLE",
    "I knew this would get you.. GAME OVER"
):
    sys.exit()

if not one_attempt(
    "What number is always the result of any digit taken to the exponent of 0?",
    "1",
    "YOU MUST GO",
    "I knew you weren't a match for me. GAME OVER"
):
    sys.exit()

if not one_attempt(
    "What is the 15th number in the fibonacci sequence?",
    "610",
    "You will not triumph against me",
    "GAME OVER PEASANT"
):
    sys.exit()

if not one_attempt(
    "1254632x12432x322x12x0x15",
    "0",
    "HOW DID YOU NOT FALL FOR IT",
    "You should have read it carefully... GAME OVER"
):
    sys.exit()

if not one_attempt(
    "How many zeros in a googol?",
    "100",
    "YOU HAVE DEFEATED ME. WELL PLAYED",
    "You came close but not close enough. WELL PLAYED. GAME OVER"
):
    sys.exit()
