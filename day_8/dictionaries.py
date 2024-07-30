def dictionary_operations():
    # create a empty dictionary called dog
    dog = {}

    # Add name, color, breed, legs, age to the dog dictionary
    dog['name'] = 'Bingo'
    dog['color'] = 'Brown'
    dog['breed'] = 'Bulldog'
    dog['legs'] = 4
    dog['age'] = 5

    # Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
    student = {
        'first_name': 'John',
        'last_name': 'Doe',
        'gender': 'male',
        'age': 25,
        'marital_status': 'single',
        'skills': ['Python', 'Java', 'JavaScript'],
        'country': 'Nigeria',
        'city': 'Lagos',
        'address': '1, Ikorodu Road, Lagos'
    }

    # Get the length of the student dictionary
    print(len(student))

    # Get the value of skills and check the data type, it should be a list
    print(type(student['skills']) == list)

    # Modify the skills values by adding one or two skills
    student['skills'].append('NodeJS')

    # Get the dictionary keys as a list
    print(student.keys())

    # Get the dictionary values as a list
    print(student.values())

    # Change the dictionary to a list of tuples using items() method
    print(student.items())

    # Delete one of the items in the dictionary
    del student['gender']
    print(student)

    # Delete the dictionary
    del student

if __name__ == '__main__':
    dictionary_operations()