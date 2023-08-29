#!/usr/bin/python

#Add new questions to the questions.txt file

def read_questions_from_file(fname):
    with open(fname, "r") as file:
        return file.read()
    
def ask_to_add_question_to_file(question):
    answer = input("Do you want to add a new question/ (y/n): ")
    if answer.lower() == "y":
        question = input("Write a new question! ")
    else:
        print("No new question added: ")
    return question
    
def check_and_add(fname, question):    
    with open(fname, "r") as file:
        initial_questions = file.read()
        if question in initial_questions:
            print("Entered question exists in file, please enter another question. ")
            return      
        correct_answer = input("Enter thw correct answer: ")
        options = input("Enter the 3 options: ")
        with open(fname, "a") as file:
            split_options = ",".join(options.split())
            file.write(f'{question}:?{correct_answer},{split_options}\n')

def main():
    fname = "questions.txt"
    print(read_questions_from_file(fname))
    question = ask_to_add_question_to_file(fname)
    check_and_add(fname, question)
    
main()


