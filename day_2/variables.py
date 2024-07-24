def variable_delcaration():
    first_name = "John"
    last_name = "Doe"
    full_name = first_name + ' ' + last_name
    country = "Finland"
    city = "Helsinki"
    age = 50
    year = 2020
    is_married = True
    is_true = True
    is_light_on = False
    # Declaring multiple variables in one line
    name, job, live = 'John Doe', 'Python Developer', 'Finland'
    print(first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on)

    # check data types of the variables
    print(type(first_name))
    print(type(last_name))
    print(type(full_name))
    print(type(country))
    print(type(city))
    print(type(age))
    print(type(year))
    print(type(is_married))

    # find the length of first_name
    print(len(first_name))

    # compare the length of first_name and last_name
    print(len(first_name) > len(last_name))

    # declare 5 as num_one and 4 as num_two
    num_one, num_two = 5, 4

    # add num_one and num_two and assign the value to a variable total
    total = num_one + num_two

    # subtract num_two from num_one and assign the value to a variable diff
    diff = num_one - num_two

    # multiply num_two and num_one and assign the value to a variable product
    product = num_two * num_one

    # divide num_one by num_two and assign the value to a variable division
    division = num_one / num_two

    # use modulus division to find num_two divided by num_one and assign the value to a variable remainder
    remainder = num_two % num_one

    # calculate num_one to the power of num_two and assign the value to a variable exp
    exp = num_one ** num_two

    # Find floor division of num_one by num_two and assign the value to a variable floor_division
    floor_division = num_one // num_two

    # print the values
    print(total, diff, product, division, remainder, exp, floor_division)

    # declare radius as 30 and assign it to a variable called radius
    radius = 30

    # calculate the area of a circle and assign the value to a variable area_of_circle
    area_of_circle = 3.14 * radius ** 2

    # calculate the circumference of a circle and assign the value to a variable circum_of_circle
    circum_of_circle = 2 * 3.14 * radius

    # print the values
    print(area_of_circle, circum_of_circle)

    # take the radius as user input and calculate the area.
    radius = float(input('Enter the radius of the circle: '))
    area_of_circle = 3.14 * radius ** 2

    # print the area
    print(area_of_circle)

    # use the built-in input function to get first name, last name, country and age from a user and store the value to their respective variable names
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    country = input('Enter your country: ')
    age = input('Enter your age: ')
    
    # print the values
    print(first_name, last_name, country, age)

if __name__ == '__main__':
    variable_delcaration()