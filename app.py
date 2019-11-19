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
    user_input = input('''5. Is this a quote from Boromir? 
                    1 for true 0 for false.
                    
                    "It is a strange fate 
                    that we should suffer so much
                    fear and doubt over so small a thing ... 
                    such a little thing"
                    
                    Answer'''
                    )
    correct_answer = 1
    if user_input == correct_answer:
        correct_answers.append("number 5")
    else:
        incorrect_answers.append("number 5")
        
#CALLING QUESTION FUNCTIONS
question1()
#question2()
#question3()
#question4()
#question5()
print("You got these questions correct: " + str(correct_answers))
print("You got these questions incorrect: " + str(incorrect_answers))