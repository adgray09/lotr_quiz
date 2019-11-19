correct_answers = []
incorrect_answers = []

#QUESTIONS
def question1():
    user_input = input(''' 1. Where is Legolas from?
                    
                    a. Mirkwood
                    b. Fangorn Forest
                    c. Lothlorian
                    d. Rivendell
                    
                    Answer: ''')
    correct_answer = "a"
    if user_input == correct_answer:
        correct_answers.append("number 1")
    else:
        incorrect_answers.append("number 1")
    
def question2():
    user_input = int(input('''2. how many Uruk-Hai fought in the battle for Helms Deep? 
                        
                    Answer: '''))
    correct_answer = 10000
    
    if user_input == correct_answer:
        correct_answers.append("number 2")
    else:
        incorrect_answers.append("number 2")
    
def question3():
    user_input = input('''3. What is Gollums original name?
                    
                    a. Marcho
                    b. Deagol
                    c. Smeagol
                    d. Falco
                    
                    Answer:''')
    correct_answer = "c"
    
    if user_input == correct_answer:
        correct_answers.append("number 3")
    else:
        incorrect_answers.append("number 3")
        
def question4():
    user_input = input('''4. How many wizards are there in middle earth?
                    
                    a. 2
                    b. 4
                    c. 5
                    d. 6
                    
                    Answer:''')
    correct_answer = "c"
    
    if user_input == correct_answer:
        correct_answers.append("number 4")
    else:
        incorrect_answers.append("number 4")
        
    
def question5():
    user_input = int(input('''5. Is this a quote from Boromir? 
                    
                    1 for true 0 for false.
                    
                    "It is a strange fate 
                    that we should suffer so much
                    fear and doubt over so small a thing ... 
                    such a little thing"
                    
                    Answer: '''
                    ))
    correct_answer = 1
    if user_input == correct_answer:
        correct_answers.append("number 5")
    else:
        incorrect_answers.append("number 5")
        
def question6():
    user_input = int(input('''6. Sauron made 4 rings of power for the elves. 
                    
                    1 for true 0 for false
                    
                    Answer:'''))
    correct_answer = 0
    
    if user_input == correct_answer:
        correct_answers.append("number 6")
    else:
        incorrect_answers.append("number 6")
                    

def question7():
    user_input = input('''7. What is the first voice you hear in the Fellowship of the Ring?
                    
                    a. Frodo
                    b. Gandalf
                    c. Galadriel
                    d. bilbo
                    
                    Answer:''')
    correct_answer = "c"
    if user_input == correct_answer:
        correct_answers.append("number 7")
    else:
        incorrect_answers.append("number 7")
        
def question8():
    user_input = input('''8. Who killed the Witch King?
                    
                    a. Eowyn
                    b. Theoden
                    c. Pippin
                    d. Arwen
                    
                    Answer:''')
    correct_answer = "a"
    if user_input == correct_answer:
        correct_answers.append("number 8")
    else:
        incorrect_answers.append("number 8")

def question9():
    user_input = int(input('''9. How many rings of power were made?
                    
                    Answer:'''))
    correct_answer = 20
    if user_input == correct_answer:
        correct_answers.append("number 9")
    else:
        incorrect_answers.append("number 9")
        
def question10():
    user_input = input('''10. How many people were in the fellowship of the ring?
                    
                    a. 7
                    b. 9
                    c. 10
                    d. 11
                    
                    Answer: ''')    
    correct_answer = "b"
    if user_input == correct_answer:
        correct_answers.append("number 10")
    else:
        incorrect_answers.append("number 10")
        
def grading():
    if len(correct_answers) > 6:
        print("You Passed! You Truely are a Lord of The Rings fan!")
    else:
        print("Sorry you didn't pass")
#CALLING QUESTION FUNCTIONS
question1()
question2()
question3()
question4()
question5()
question6()
question7()
question8()
question9()
question10()
print("You got these questions correct: " + str(correct_answers))
print("You got these questions incorrect: " + str(incorrect_answers))

grading()