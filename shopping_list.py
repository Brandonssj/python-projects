#This is just a little cool shopping list program that can be run at the terminal.

shopping_list = []

print("""Heya! Today we are going to make a shopping list!
You can put whatever item you may require in this shopping list.Chelse
Type "DONE" when you are done adding items to your shopping list""")

while True:
    user_input = input("> ")
    if user_input == "DONE":
        sure = input("Are you sure you want to quit?\nType \"no\" to keep adding items and yes to quit.\n")
        if sure == "no" or sure == "NO":
            continue
        else:
            break
    else:
        shopping_list.append(user_input)


print("Here are all of the items in your shopping list:")

for items in shopping_list:
    print(items)

print("\nThanks for playing!\nGoodbye!!  :)")
