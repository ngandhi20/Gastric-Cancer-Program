import pandas as pd
from funcs import preprocessing_tasks, option1, option2

gastric_data = pd.read_csv("gastric_cancer_program/data/gastric_cancer_detection_dataset.csv",
                           keep_default_na=False,
                           na_values=['', ' '])    # Making sure pandas doesn't change 'None' values to NaN              

data = preprocessing_tasks(gastric_data)

print("""
    Welcome to my program that analyzes the gastric cancer dataset!
    
    Here are two things you can do with your dataset!
    Option #'s
    1 - choose a characteristic and see how it relates to having cancer or not
    2 - choose 2 characteristics and compare it to the cancer rate
    """)

okay_answer = False
while okay_answer == False:
    option = input("Choose an option! (1 or 2): ").strip()
    if option in ['1', '2'] or option in [1, 2]:      
        if int(option) == 1:
            option1(data)
            okay_answer = True
        elif int(option) == 2:
            option2(data)
            okay_answer = True
    else:
        print("No! Try again!\n")
