correct_answers = []
incorrect_answers = []


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
    user_input = input('''What is Gollums original name?
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
    
                    
    
    #calling questions
question1()
question2()
question3()
print(correct_answers)
print(incorrect_answers)