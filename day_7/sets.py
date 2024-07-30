def sets_operations():
    # sets
    it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
    A = {19, 22, 24, 20, 25, 26}
    B = {19, 22, 20, 25, 26, 24, 28, 27}
    age = [22, 19, 24, 25, 26, 24, 25, 24]

    # Find the length of the set it_companies
    print(f'it_companies length: {len(it_companies)}')

    # Add 'Twitter' to it_companies
    it_companies.add('Twitter')

    # Insert multiple IT companies at once to the set it_companies
    it_companies.update(['LinkedIn', 'Snapchat'])

    # Remove one of the companies from the set it_companies
    it_companies.remove('IBM')

    # What is the difference between remove and discard
    # remove() raises an error if the item is not found in the set
    # discard() does not raise an error if the item is not found in the set

    # Join A and B
    print(f'A union B: {A.union(B)}')

    # Find A intersection B
    print(f'A intersection B: {A.intersection(B)}')

    # Is A subset of B
    print(f'A subset of B: {A.issubset(B)}')

    # Are A and B disjoint sets
    print(f'A and B disjoint sets: {A.isdisjoint(B)}')

    # Join A with B and B with A
    print(f'A union B: {A.union(B)}')
    print(f'B union A: {B.union(A)}')

    # What is the symmetric difference between A and B
    print(f'A symmetric difference B: {A.symmetric_difference(B)}')
    print(f'B symmetric difference A: {B.symmetric_difference(A)}')

    # Delete the sets completely
    del A
    del B

    # Convert the ages to a set and compare the length of the list and the set, which one is bigger?
    print(f'age length: {len(age)}')
    print(f'age set length: {len(set(age))}')
    
    # Explain the difference between the following data types: string, list, tuple and set
    # String: A string is a sequence of characters
    # List: A list is a collection of items which are ordered and changeable
    # Tuple: A tuple is a collection of items which are ordered and unchangeable
    # Set: A set is a collection of items which are unordered and unindexed

    # I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
    sentence = 'I am a teacher and I love to inspire and teach people'
    print(f'Unique words in the sentence: {len(set(sentence.split()))}')


if __name__ == '__main__':
    sets_operations()