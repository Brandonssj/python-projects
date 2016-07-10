#This is just a little cool shopping list program that can be run at the terminal.
# Below is the first version of the program.
# shopping_list = []
#
# print("""Heya! Today we are going to make a shopping list!
# You can put whatever item you may require in this shopping list.
# Type "DONE" when you are done adding items to your shopping list""")
#
# while True:
#     user_input = input("> ")
#     if user_input == "DONE":
#         sure = input("Are you sure you want to quit?\nType \"no\" to keep adding items and yes to quit.\n")
#         if sure == "no" or sure == "NO":
#             continue
#         else:
#             break
#     else:
#         shopping_list.append(user_input)
#
#
# print("Here are all of the items in your shopping list:")
#
# for items in shopping_list:
#     print(items)
#
# print("\nThanks for playing!\nGoodbye!!  :-)")

#This is the current version

shopping_list = []

def start():
    print("""Heya! Today we are going to make a shopping list!
You can put whatever item you may require in this shopping list.
Type "DONE" when you are done adding items to your shopping list,
"HELP" if you need help, and "SHOW" to see what you currently have in your list.""")

def show():
    for item in shopping_list:
        print(item)

def help():
    print("Type 'DONE' when you are finish add items to your list!\nType 'SHOW' to see what you currectly have inside your list.")

def add_to_list(input):
    shopping_list.append(input)
    print("Added {}. Shopping list now has {} items.".format(user_input, len(shopping_list)))

start()

while True:
    user_input = input("> ")
    if user_input == "DONE":
        sure = input("Are you sure you want to quit?\nType \"no\" to keep adding items and yes to quit.\n")
        if sure == "no" or sure == "NO":
            continue
        else:
            break
    elif user_input == "HELP":
        help()
        continue
    elif user_input == "SHOW":
        print("You currently have {} items in you list:".format(len(shopping_list)))
        show()
        continue
    add_to_list(user_input)


print("Here are all of the items in your shopping list:")

show()

print("\nThanks for playing!\nGoodbye!!  :-)")
