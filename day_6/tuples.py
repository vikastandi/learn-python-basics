def tuple_operations():
    # Create an empty tuple
    empty_tuple = ()

    # Create a tuple containing names of your sisters
    sisters = ('Jane', 'Mary', 'Linda')

    # Create a tuple containing names of your brothers
    brothers = ('John', 'Peter', 'Tom')

    # Join brothers and sisters tuples and assing it to siblings
    siblings = brothers + sisters

    # How many siblings do you have?
    print(f'I have {len(siblings)} siblings')

    # Modify the siblings tuple and add the name of your father and mother and assign it to family_members
    family_members = ('Dad', 'Mum') + siblings

    # unpack siblings ans parents from family_members
    parents, *siblings = family_members

    # Create fruits, vegetables and animal products tuples
    fruits = ('Apple', 'Banana', 'Orange')
    vegetables = ('Carrot', 'Spinach', 'Kale')
    animal_products = ('Eggs', 'Milk', 'Meat')

    # Join the three tuples and assign it to food_stuff_tp
    food_stuff_tp = fruits + vegetables + animal_products

    # Change the food_stuff_tp tuple to a food_stuff_lt list
    food_stuff_lt = list(food_stuff_tp)

    # Slice out the first three items from the food_stuff_tp tuple
    first_three = food_stuff_tp[:3]

    # Slice out the last three items from the food_stuff_tp tuple
    last_three = food_stuff_tp[-3:]

    # Delete the food_staff_tp tuple
    del food_stuff_tp

    # Check if an item exist in tuple:
    # Check if 'Estonia' is a nordic country
    # Check if 'Iceland' is a nordic country
    # nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
    nordic_countries = ('Denmark', 'Finaland', 'Iceland', 'Norway', 'Sweden')
    print('Estonia' in nordic_countries)
    print('Iceland' in nordic_countries)
    

if __name__ == '__main__':
    tuple_operations()