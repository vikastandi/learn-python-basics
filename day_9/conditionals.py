def conditionals():
    # Get user input using input("Enter your age: "). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the remaining years
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are old enough to drive")
    else:
        print(f"Wait for {18 - age} years")

    # Write a code which gives grade to students according to theirs scores:
    # 80-100: A
    # 70-89: B
    # 60-69: C
    # 50-59: D
    # 0-49: F
    score = int(input("Enter your score: "))
    if score >= 80 and score <= 100:
        print("grade A")
    elif score >= 70 and score <= 79:
        print("grade B")
    elif score >= 60 and score <= 69:
        print("grade C")
    elif score >= 50 and score <= 59:
        print("grade D")
    elif score >= 0 and score <= 49:
        print("grade F")
    else:
        print("Invalid score")

    # Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
    # September, October or November, the season is Autumn.
    # December, January or February, the season is Winter.
    # March, April or May, the season is Spring
    # June, July or August, the season is summer
    season = input("Enter the month: ")
    if season in ['September', 'October', 'November']:
        print("Autumn")
    elif season in ['December', 'January', 'February']:
        print("Winter")
    elif season in ['March', 'April', 'May']:
        print("Spring")
    elif season in ['June', 'July', 'August']:
        print("Summer")
    else:
        print("Invalid month")

    # The following list contains some fruits:
    # fruits = ['banana', 'orange', 'mango', 'lemon']
    # If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruit = input("Enter a fruit: ")
    if fruit not in fruits:
        fruits.append(fruit)
        print(fruits)
    else:
        print("That fruit already exist in the list")

    # here we have a person dictionary. Feel free to modify it!
    # person = {
    #     'first_name': 'Asabeneh',
    #     'last_name': 'Yetayeh',
    #     'age': 250,
    #     'country': 'Finland',
    #     'is_marred': True,
    #     'skills':  ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    #     'address': {
    #         'street': 'Space street',
    #         'zipcode': '02210'
    #     }
    # }
    person = {
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_marred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }

    # Check if the person dicitionary has skills key, if so print out the middle skill in the skills list.
    if 'skills' in person:
        print(person['skills'][len(person['skills']) // 2])

    # Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result
    if 'skills' in person:
        print('Python' in person['skills'])

if __name__ == '__main__':
    conditionals()