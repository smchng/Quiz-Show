# Week 4 Coding Exercise CMPT 120 D300
# Calculate This, Computer!
# Samantha Chung
# Oct 3 2020

# For this assignment, you will be participating in a quiz game. In the beginning you will go through an eligibility quiz to see if you qualify. It will not be for points. After the questions, the real quiz will begin. 5 questions will be asked. To pass, you must get at least 3 questions right. #


print ("Hello! Welcome to a third grader quiz. Are you smarter than a third grader?")
print ("Let's find out! Would you like to play?")
begin = input().lower().strip('!?.,')

# Asks if they would like to begin the game
if begin == 'yes' or begin == 'ok' or begin == 'sure':
  print ("Perfect! Now we will begin with a qualification question. Are you ready?")
  input ("Press 'Enter' To Begin_")
  # The moment the user presses enter, the code clears and qualification question will begin
  replit.clear()
  print ("The qualifications will have multiple questions related to each other.")
  print ("If you answer correct, you can continue. If not you will not qualify and exit the game.")
  print ("This is the qualification question:")
  print ("What does 2 + 3 = ")
  # I turn the answer in to a float because as a string, it does not recognize the answer as 5
  qualify_1 = float(input())
  # Answer must be integer
  if qualify_1 == 5:
    print ("Correct!")
    print ("Now take your previous answer and add 3.6.")
    # Answer is changed to float because the correct answer will contain a decimal
    qualify_2 = float(input())
    if qualify_2 == qualify_1 + 3.6:
      print ("Correct!\nNow take that number again multiply it by 6.23")
      print ("What do you get?")
      qualify_3 = float(input())
      if qualify_3 == qualify_2 * 6.23:
        print ("Correct again!")
        print ("You have completed all of the qualification questions.")
        print ("The quiz will have 5 questions. You must get 3 correct to pass.")
        input ("Press 'Enter' To Begin the Quiz_")
        replit.clear()


# Real quiz begins and points will be counted
        # Question list
        questions = ["Please solve this equation: (5+7)*2/4+3 = ?", "How many minutes are in 6 hours?", "How many dollars in 3675 nickels? (Please answer to 2 decimal places)", "Which number is larger -36 or 2?"]
        answers = [9, 360, 183.38, 2]
        # Statement to move the printed question and answer to next one
        question_number = 0
        # Score to keep track of wrong and rigth answers
        score = 0
# Loop to ask each question and line up with answer
        for q in questions:
          print (q)
          reply = float(input())
          # Result if answer is correct
          # Picks and chooses quesions and answer so only the right answer is allowed
          if reply == answers[question_number]:
            score = score + 1
            print ("Correct!\nThis is the next question:")
          # Result is answer is wrong
          else:
            print ("Incorrect.")
            print ("You lost 1 point.")
            print ("Here is the next question.")
          question_number += 1

# Extra question after the loop to not repeat "Here is the next question." It is also isn't a math problem so int is an error
        print ("Name a country in Scandanavia.")
        answer_scandanavia = input().lower().strip("?!,.")
        # Plausible answers
        if answer_scandanavia == 'sweden' or answer_scandanavia == 'denmark' or answer_scandanavia == 'norway':
          score = score + 1
          print ("Correct!")
        else:
          print ("Incorrect")
          print ("You lost one point")

        print ("You have completed the quiz.")
        input ("Press 'Enter' to reveal score.")
# Final code to diplay score and calculate percentage
        replit.clear()
        print ("You got", str(score) + "/5")
        print ("That is", str(score/5*100) + "%")
# Uses conditional to see if you are smarter than a third grader or not with > < = statements
        if score < 3:
          print ("OH NO! You are not smarter than a third grader.")
        elif score == 3:
          print ("You passed the quiz but... I can't really say if you are smarter than a third grader...")
        elif score > 3:
          print ("Good. You are smarter than a third grader!")
        print ("Thank you for playing! Goodbye!")


    # I used great than or less than so input could accept numbers with and without decimals. Using the regular == would create error
    elif qualify_2 < 3.6 or qualify_2 > 3.6:
      print ("Your answer is incorrect. The answer was '8.6'\nYou are not qualified for this game. Goodbye.")
  elif qualify_1 < 5 or qualify_1 > 5:
    print ("Your answer is incorrect. The answer was '5'\nYou are not qualified for this game. Goodbye.")


# Other replies will not start the game and end the code
elif begin == 'no':
  print ("That's ok. I understand if you are not up to the challenge. Goodbye.")
else:
  print ("I do not understand. Quiz cancelled. Goodbye.")
