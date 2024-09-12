"""This is a program that plans a Tea Party"""
__author__ : str = "730768561"


def main_planner(guests : int) -> None: 
    """Calls each function and produces the output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people = guests)))
    print("Treats: " + str(treats(people = guests)))
    print("Cost: $" + str(cost(tea_count = tea_bags(people = guests), treat_count = treats(people = guests)))) #This statement was also challenging since I had to utilize and call multiple functions in one line.

def tea_bags(people : int) -> int: 
    """Computes the number of teabags needed based on the number of guests"""
    return people * 2

#It took be quite some time to figure out that I had to call the tea_bags function inside the treats function.
#I figured that this method helps abstract the code and make it more readable for users. 
def treats(people : int) -> int: 
    """Computer the number of treats needed based on the numbers of teas guests will drink"""
    return int(tea_bags(people = people) * 1.5)


def cost(tea_count:int, treat_count:int) -> float: 
    """Computes the cost of teabags and treats combined"""
    return tea_count * 0.5 + treat_count * 0.75

#At first I didn't understand why you could put this function at the top, 
#but after testing it I realized that the main_planner function wouldn't have been defined 
#which would cause the program to not run. 
if __name__ == "__main__": 
    main_planner(guests = int(input("How many guests are attending your party? ")))
