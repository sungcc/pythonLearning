weight = float(input('please enter your weight in KG\n'))
height = float(input('please enter your height in CM\n'))
userName = str(input('please enter your name\n'))
height = height/100
bmi = weight / (height*height)

if bmi > 0:
    if bmi < 18.5:
        print(f"Your bmi is {bmi}, you are underweight!")
    elif bmi < 25:
        print(f"Your bmi is {bmi}, you are healthy!") 
    elif bmi < 30:
        print(f'Your bmi is {bmi}, you are obese')
    else: 
        print(f'Your bmi is {bmi}, you are servely obese')
    
