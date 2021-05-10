'''
let's figure out given a room of k people, what's the probability at least 2 people will have the same birthday
'''

# load some libs
import math

# let's implement a function that takes in a argument: number of people in a room


def two_people_same_birthday(k):

    if k == 0:
        print("No one in the room")

    elif k < 0:
        print("Are there anti-people in the room?")

    elif k == 1:
        print("Has to be greater than one person in the room")

    elif k >= 2:

        print(
            f"Probability of {k} people in a room where everyone has distinct birthday is: ")
        probability_distinct_birthday = math.factorial(
            365) / (math.factorial(365 - k) * (365)**k)
        print(probability_distinct_birthday)

        print(
            f"Probability of {k} people in a room having at least 2 people having the same birthday is: ")
        probability_of_at_least_two_have_the_same = 1 - probability_distinct_birthday

        return probability_of_at_least_two_have_the_same
