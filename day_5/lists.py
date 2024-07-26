def lists_operations():
    # Declare an empty list named empty_list
    empty_list = []

    # Declare a list with more than 5 items
    more_than_five_items = [1, 2, 3, 4, 5, 6]

    # Find the length of the list
    print(len(more_than_five_items))

    # Get the first item, the middle item and the last item of the list
    print(more_than_five_items[0])
    print(more_than_five_items[len(more_than_five_items) // 2])
    print(more_than_five_items[-1])

    # Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
    mixed_data_types = ['John', 25, 1.75, 'Single', 'Nairobi']

    # Declare a list variable name it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
    it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

    # Print the list using print()
    print(it_companies)


    # Print the number of companies in the list
    print(len(it_companies))

    # Print the first, middle and last company
    print(it_companies[0])
    print(it_companies[len(it_companies) // 2])
    print(it_companies[-1])

    # Print the list after modifying one of the companies
    it_companies[0] = 'Twitter'
    print(it_companies)

    # Add an IT company to it_companies
    it_companies.append('LinkedIn')

    # Insert an IT company in the middle of the companies list
    it_companies.insert(len(it_companies) // 2, 'Slack')


    # Change one of the it_companies to uppercase (IBM excluded!)
    it_companies[1] = it_companies[1].upper()

    # Join the it_companies with a string '#;'
    print('#;'.join(it_companies))

    # Check if a certain company exists in the it_companies list.
    print('Microsoft' in it_companies)

    # Sort the list using sort() method
    it_companies.sort()
    print(it_companies)

    # Reverse the list in descending order using reverse() method
    it_companies.reverse()
    print(it_companies)

    # Slice out the first 3 companies from the list
    print(it_companies[:3])

    # Slice out the last 3 companies from the list
    print(it_companies[-3:])

    # Remove the first IT company from the list
    it_companies.pop(0)

    # Remove the middle IT company or companies from the list
    it_companies.pop(len(it_companies) // 2)

    # Remove the last IT company from the list
    it_companies.pop()

    # Remove all IT companies from the list
    it_companies.clear()

    # Join the following lists:
    # front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    # back_end = ['Node','Express', 'MongoDB']
    front_end = ['HTML, ' 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node', 'Express', 'MongoDB']
    full_stack = front_end + back_end
    print(full_stack)

    # insert Python and SQL after Redux
    full_stack.append('Python')
    full_stack.append('SQL')

    # The following is a list of 10 students ages:
    # ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

    # Sort the list and find the min and max age
    ages.sort()
    print(f'min: {ages[0]}, max: {ages[-1]}')

    # Add the min age and the max age again to the list
    ages.append(ages[0])
    ages.append(ages[-1])

    # Find the median age (one middle item or two middle items divided by two)
    ages.sort()
    print(ages[len(ages) // 2])

    # Find the average age (sum of all items divided by their number )
    print(sum(ages) / len(ages))

    # Find the range of the ages (max minus min)
    print(ages[-1] - ages[0])

    # Compare the value of (min - average) and (max - average), use abs() method
    avg = sum(ages) / len(ages)
    print(abs(ages[0] - avg) > abs(ages[-1] - avg))

    # ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries
    china, russia, usa, *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
    print(china, russia, usa, scandic_countries)

if __name__ == '__main__':
    lists_operations()