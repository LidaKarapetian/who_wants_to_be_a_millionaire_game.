#!/usr/bin/python

import random

#A function to read data from a questions.txt file and convert it to an list
def read_questions(filename):
    questions = []
    with open(filename, "r") as file:
        for el in file:
            questions.append(el.strip())
    return questions

#A function to generate 10 random questions
def random_questions(questions):
    game_questions = []
#
    while len(game_questions) < 10:
        num = random.randint(0, len(questions) - 1)
        if questions[num] not in game_questions:
            game_questions.append(questions[num])
    return game_questions

#A function returns dictionary in which are questions and answers in list
def questions_and_answers_in_dictionary(game_questions):
    gquestions = {}
    for el in game_questions:
        q,a = el.split("?")
        gquestions[q] = a.split(",")
    return gquestions

#Game control function
def play_game(gquestions):
    cnt = 0

    variant = ["A", "B", "C", "D"]
    cvariant = ""
    for q,a in gquestions.items():
        print(q)
        correct = a[0]
        random.shuffle(a)
        for i in range(len(variant)):
            print(variant[i], a[i])
            if a[i] == correct:
                cvariant = variant[i]
        answer = input("Your variant: ")
        if answer.upper() == cvariant:
            cnt += 1
            print("Correct.")
        else:
            print("Not. Correct answer was: ", correct)
    print("You got %d/10" %cnt)
 

def main():
    questions =read_questions("questions.txt")
    game_questions = random_questions(questions)
    gquestion = questions_and_answers_in_dictionary(game_questions)
    play_game(gquestion)
  
main()

    


