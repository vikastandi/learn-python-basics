# import file countries.py
from countries import countries

# import file countries_data.py
from countries_data import countries_data

def loop_operations():
    # Iterate 0 to 10 using for loop, do the same using while loop.
    for i in range(11):
        print(i, end=' ')
    print()
    i = 0
    while i < 11:
        print(i, end=' ')
        i += 1
    print()

    # Iterate 10 to 0 using for loop, do the same using while loop.
    for i in range(10, -1, -1):
        print(i, end=' ')
    print()
    i = 10
    while i >= 0:
        print(i, end=' ')
        i -= 1
    print()

    # Write a loop that makes seven calls to print(), so we get on the output the following triangle:
    # #
    # ##
    # ###
    # ####
    # #####
    # ######
    # #######
    for i in range(1, 8):
        print('#' * i)

    # Use nested loops to create the following:
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    for i in range(0, 8):
        for j in range(0, 8):
            print('#', end=' ')
        print()
    print()

    # Print the following pattern:
    # 0 x 0 = 0
    # 1 x 1 = 1
    # 2 x 2 = 4
    # 3 x 3 = 9
    # 4 x 4 = 16
    # 5 x 5 = 25
    # 6 x 6 = 36
    # 7 x 7 = 49
    # 8 x 8 = 64
    # 9 x 9 = 81
    # 10 x 10 = 100
    for i in range(0, 11):
        print(f'{i} x {i} = {i * i}')

    # Iterate through the list, ['Python', Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
    for item in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:
        print(item)
    
    # Use for loop to iterate from 0 to 100 and print only even numbers
    for i in range(0, 101, 2):
        print(i, end=' ')
    print()

    # Use for loop to iterate from 0 to 100 and print only odd numbers
    for i in range(1, 101, 2):
        print(i, end=' ')
    print()

    # Use for loop to iterate from 0 to 100 and print the sum of all numbers.
    total = 0
    for i in range(101):
        total += i
    print(f'The sum of all numbers is {total}')

    # use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
    sum_of_evens = 0
    sum_of_odds = 0
    for i in range(101):
        if i % 2 == 0:
            sum_of_evens += i
        else:
            sum_of_odds += i
    print(f'The sum of all evens is {sum_of_evens}')
    print(f'The sum of all odds is {sum_of_odds}')

    # Loop through the countries and extract all the countries containing the word land.
    for country in countries:
        if 'land' in country:
            print(country)

    # This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
    reversed_fruits = []
    fruits = ['banana', 'orange', 'mango', 'lemon']
    for fruit in range(len(fruits) - 1, -1, -1):
        reversed_fruits.append(fruits[fruit])
    print(reversed_fruits)

    # What is the total number of languages in the countries data
    total_languages = set()
    for country in countries_data:
        total_languages.update(country['languages'])
    print(len(total_languages))

    # Find the ten most spoken languages from the data
    languages = {}
    for country in countries_data:
        for language in country['languages']:
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1
    print(sorted(languages.items(), key=lambda x: x[1], reverse=True)[:10])

    # Find the 10 most populated countries
    countries_population = {}
    for country in countries_data:
        countries_population[country['name']] = country['population']
    print(sorted(countries_population.items(), key=lambda x: x[1], reverse=True)[:10])

if __name__ == '__main__':
    loop_operations()