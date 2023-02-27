# create a dictionary to have key (food name) with value (price)
# how to create a dictionary in python
# ('key': value), ('key': value)

### GREETING
print("*" * 50)
print("Welcome! From the READ.ME file, you can see the list of meals. To see the price, simply type in the name of the dish.")
print()

### GLOBAL VARIABLES
MENU = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesdadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

TOTAL_AMOUNT = 0


### FUNCTION DEFINITION

def query_user() -> str:
    '''
    param: void
    returns: lowercased user input
    rtype: str
    '''

    # query user input
    user_inp = str(input("Item: "))

    # lowercase everything to start
    user_inp.lower()

    return user_inp

def main():
    i = 0
    total = 0

    # infinite loop
    while (True):
        try:
            # get user input
            new_food = Food(query_user())
            title = new_food.get_title()

            new_food.set_name(title)

            if new_food.get_name() in MENU:
                # keep track of user inputs
                food_list = list()

                # add user input as object to food list
                food_list.append(new_food)

                total += new_food.get_price()

                print(f"Total: ${total:.2f}")

                i += 1

        except EOFError:
            # when error occurs (nullpointer)
            print()
            break

    return



### STARTING PROGRAM
main()


### GOODBYE

print()
print("Thank you for looking through the menu!")
print("You have looked through...")

# print dictionary
for i in range (len(food_list)):
    print(food_list[i].get_members())


print("*" * 50)