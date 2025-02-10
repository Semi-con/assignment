import random

maths_question = [("1 + 2 = ?", 3), ("10 - 6 = ?", 4), ("8 / 2 = ?", 4), ("6 + 4 = ?", 10), ("7 + 3 = ?", 10),
                  ("12 - 4 = ?", 8), ("3 * 4 = ?", 12), ("8 - 2 = ?", 6), ("12 + 4 = ?", 16), ("8 + 7 = ?", 15),
                  ("9 + 8 = ?", 17), ("13 - 4 = ?", 9), ("8 * 2 = ?", 16), ("7 - 4 = ?", 3), ("17 - 13 = ?", 4)]

sampled_questions = random.sample(maths_question, 5)
answered, correct = 0, 0

print("------ Welcome to the maths answering system (within 20) -----")
print("You are needed to answer 5 questions.\n\n")
while answered < 5:
    print("Question {}: {}".format(answered+1, sampled_questions[answered][0]))
    while True:
        try:
            val = eval(input("Your answer is: "))
            if val == sampled_questions[answered][1]:
                print("Correct answer\n")
                correct += 1
            else:
                print("Answer not correct! The correct answer should be {}\n".format(sampled_questions[answered][1]))
            answered += 1
            break
        except:
            print("Please use numbers as the input")

print("Questions finished. You got {} scores".format(int((correct/answered)*100)))


