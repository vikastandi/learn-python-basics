def string_operations():
    # Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
    thirty_days_of_python = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'

    # Declare a variable named company and assign it to an initial value "Coding For All".
    company = 'Coding For All'

    # Print the variable company using print()
    print(company)

    # Print the length of the company string using len() method and print()
    print(len(company))

    # Change all the characters of the string to uppercase, using upper() method
    print(company.upper())

    # Change all the characters of the string to lowercase, using lower() method
    print(company.lower())

    # Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
    print(company.capitalize())
    print(company.title())
    print(company.swapcase())

    # Check if Coding For All string contains Coding using the method index, find or other methods.
    print(company.index('Coding'))
    print(company.find('Coding'))
    print('Coding' in company)

    # Replace the word coding in the string "Coding For All" to Python.
    print(company.replace('Coding', 'Python'))

    # Change Python for Everyone to Python for All using the replace method or other methods.
    python_for_everyone = 'Python for Everyone'
    print(python_for_everyone.replace('Everyone', 'All'))

    # Split the string 'Coding For All' using space as the separator (split())
    print(company.split())

    # "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
    companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
    print(companies.split(', '))

    # What is the character at index 0 in the string Coding For All.
    print(company[0])

    # What is the last index of the string Coding For All.
    print(company[-1])

    # What character is at index 10 in "Cofing For All" string.
    print(company[10])

    # Create an acronym or an abbreviation for the name "Python For Everyone".
    python_for_everyone = 'Python For Everyone'
    print(python_for_everyone.split()[0][0] + python_for_everyone.split()[1][0] + python_for_everyone.split()[2][0])

    # Use index to determine the position of the first occurrence of C in Coding For All.
    print(company.index('C'))

    # use rfind to find the last occurrence of l in Coding For All People.
    company_people = 'Coding For All People'
    print(company_people.rfind('l'))

    # Use index or find to find the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
    sentence = 'You cannot end a sentence with because because because is a conjunction'
    print(sentence.index('because'))
    print(sentence.find('because'))

    # Use rindex to find the position of the last occurrence of the work because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
    print(sentence.rindex('because'))

    # Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjuction'
    sentence[0:sentence.index('because')-1] + sentence[sentence.rindex('because')+len('because'):]

    # Does ''Coding For All' start with a substring Coding?
    print(company.startswith('Coding'))

    # Does 'Coding For All' end with a substring coding?
    print(company.endswith('coding'))

    # '   Coding For All      '  remove the left and right trailing spaces in the given string.
    print('   Coding For All      '.strip())

    # Which one of the following variables return True when we use the method isidentifier(): 30DaysOfPython, thirty_days_of_python
    print('30DaysOfPython'.isidentifier())
    print('thirty_days_of_python'.isidentifier())

    # The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string
    python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
    print(' # '.join(python_libraries))

    # Use the new line escape sequence to separate the following sentence: 'I am enjoying this challenge. I just wonder what is next.'
    print('I am enjoying this challenge.\nI just wonder what is next.')

    # Use a tab escape sequence to write the following lines. Do not use space to align the sentences.
    # Name      Age     Country     City
    # Asabeneh  250     Finland     Helsinki
    print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

    # Use the string formatting method to display the following:
    # radius = 10
    # area = 3.14 * 10 ** 2
    # The area of a circle with radius 10 is 314 meters square.
    radius = 10
    area = 3.14 * radius ** 2
    print(f'The area of a circle with radius {radius} is {area} meters square.')

    # Make the following using string formatting methods:
    # 8 + 6 = 14
    # 8 - 6 = 2
    # 8 * 6 = 48
    # 8 / 6 = 1.33
    # 8 % 6 = 2
    # 8 // 6 = 1
    # 8 ** 6 = 262144
    a = 8
    b = 6
    print(f'{a} + {b} = {a+b}')
    print(f'{a} - {b} = {a-b}')
    print(f'{a} * {b} = {a*b}')
    print(f'{a} / {b} = {a/b:.2f}')
    print(f'{a} // {b} = {a//b}')
    print(f'{a} ** {b} = {a**b}')


if __name__ == "__main__":
    string_operations()