import numpy as np
import matplotlib.pyplot as plt

def preprocessing_tasks(gastric_data):
    # remove null values
    gastric_data.dropna(inplace=True)

    # remove duplicate rows
    gastric_data.drop_duplicates(inplace=True)

    # remove columns useless to the program
    gastric_data.drop(gastric_data.iloc[:, -19:-1], axis = 1, inplace = True) # columns -19 to -2 are not useful to this program

    return gastric_data


def option1(data: list[list]):
    '''
    user chooses a category then gets a bar plot of the percentage of cancerous vs. non-cancerous
    '''
    user_input = False
    while user_input == False:
        characteristic = input("""
        gender,
        ethnicity,
        geographical_location,
        family_history,
        smoking_habits,
        alcohol_consumption,
        helicobacter_pylori_infection,dietary_habits,
        existing_conditions,
        \nChoose a characteristic : """)
        if len(characteristic.split()) > 1:
            print("Only one characteristic please!")
            user_input = False
        elif characteristic not in data.columns:
            print(f"Column '{characteristic}' not found in data!")
            user_input = False
        else:
            user_input = True

    cat_filt = data[characteristic]
    unique_values_test = list(set(cat_filt))
    unique_values_test.sort()

    percentages_listed = []
    percent_of_ok = []
    category_labels = []
    
    for value in unique_values_test:
        filtered_data = data[cat_filt == value]
        total_in_cats = len(filtered_data)\

        if total_in_cats == 0:
            continue

        total_cancerous = filtered_data['label'].sum()
        percentage_of_cancerous = ((total_cancerous / total_in_cats) * 100)
        category_labels.append(str(value)) #convert to stirng for display
        percentages_listed.append(percentage_of_cancerous)
        percent_of_ok.append(100 - percentage_of_cancerous)

    plot_data_universal(category_labels, percentages_listed, percent_of_ok, characteristic)
    

def option2(data: list[list]):
    '''
    user chooses 2 categories an gets a bar plot
    '''

    user_input = False
    while user_input == False:
        two_characters = input("""
            gender,
            ethnicity,
            geographical_location,
            family_history,
            smoking_habits,
            alcohol_consumption,
            helicobacter_pylori_infection,
            dietary_habits,
            existing_conditions,
            \nChoose two characteristics: """).split()
        if len(two_characters) > 2:
            print("Only two characteristics please!")
            user_input = False
        else:
            valid = True
            for categ in two_characters:
                if categ not in data.columns:
                    print(f"Column '{categ}' not found in data!")
                    valid = False
            if valid:
                user_input = True
    

    one_cat = data[two_characters[0]]
    two_cat = data[two_characters[1]]
    unique_values_1 = list(set(one_cat))
    unique_values_2 = list(set(two_cat))
    unique_values_1.sort()  #.sort() alteres the original list!
    unique_values_2.sort()

    percentages_listed = []
    percent_of_ok = []
    category_labels = []
    for val_one_cat in unique_values_1: # female, male
        for val_two_cat in unique_values_2: # ethA, ethB, ethC
            filtered_data = data[(one_cat == val_one_cat) & (two_cat == val_two_cat)]
            total_in_cats = len(filtered_data)
            total_cancerous = filtered_data['label'].sum()
            percentage_of_cancerous = ((total_cancerous / total_in_cats) * 100)
            category_labels.append(f"{val_one_cat}, {val_two_cat}")
            percentages_listed.append(percentage_of_cancerous)
            percent_of_ok.append(100 - percentage_of_cancerous)

    plot_data_universal(category_labels, percentages_listed, percent_of_ok, two_characters)


def plot_data_universal(category_labels, cancerous_pct, number_of_ok, category_of_choosing):
    x = np.arange(len(category_labels))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot bars side by side
    bars1 = ax.bar(x - width/2, cancerous_pct, width, label='Cancerous', color='red')
    bars2 = ax.bar(x + width/2, number_of_ok, width, label='Non-Cancerous', color='green')
    
    # Customize the plot
    ax.set_xlabel('Groups')
    ax.set_ylabel('Percentage (%)')
    ax.set_title(f'Cancerous vs Non-Cancerous for {category_of_choosing}')
    ax.set_xticks(x)
    ax.set_xticklabels(category_labels)
    ax.legend()
    
    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}%', ha='center', va='bottom')
    
    for bar in bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}%', ha='center', va='bottom')
    
    ax.grid(True, axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()