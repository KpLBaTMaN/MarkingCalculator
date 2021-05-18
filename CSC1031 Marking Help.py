# By Andrew Brown
print("This script to help mark May 2021 exam paper")
print("*******")
print("Count the answers they have correct and this will output the mark for each question")


# Variables
questionsScore = []
questionMarks = []


def main():
    print("Enter in the scores for each question as it appears in order")
    question1_method()
    question2_method()
    question3_method()
    question4_method()
    question5_method()
    question6_method()
    question7_method()
    question8_method()
    printScores()
    printMarks()
    calculateMark()
    resetVariables()
    main()


def resetVariables():
    questionsScore.clear()
    questionMarks.clear()


def question1_method():
    questionsScore.append(input("Q1: "))
    questionMarks.append((int(questionsScore[0])/10) * 12)


def question2_method():
    questionsScore.append(input("Q2: "))
    questionMarks.append((int(questionsScore[1])/11) * 16)


def question3_method():
    questionsScore.append(input("Q3: "))
    questionMarks.append((int(questionsScore[2])/11) * 12)


def question4_method():
    questionsScore.append(input("Q4: "))
    questionMarks.append((int(questionsScore[3])/6) * 12)


def question5_method():
    questionsScore.append(input("Q5: "))
    questionMarks.append((int(questionsScore[4])/10) * 12)


def question6_method():
    questionsScore.append(input("Q6: "))
    questionMarks.append((int(questionsScore[5])/8) * 12)


def question7_method():
    questionsScore.append(input("Q7: "))
    questionMarks.append((int(questionsScore[6])/6) * 12)


def question8_method():
    questionsScore.append(input("Q8: "))
    questionMarks.append((int(questionsScore[7])/7) * 12)


def printScores():
    print("Scores of student")
    for x in range(len(questionsScore)):
        print(str(questionsScore[x]))


def printMarks():
    print("Marks of student")
    for y in range(len(questionMarks)):
        print(str(round(questionMarks[y], 2)))


def calculateMark():
    total = 0.0

    for y in questionMarks:
        total += y
    print("Total: " + str(round(total, 2)))


if __name__ == '__main__':
    main()
