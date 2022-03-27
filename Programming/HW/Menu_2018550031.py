#%%
def sort_menu(menu):
    """I found a problem in sorting list matrix cuz there is no key in list.
    So I decided to make a dictionary for sorting."""
    menu_mapping = {}
    for i in range(len(menu[0])):
        menu_mapping[menu[1][i]] = menu[0][i]  # I make prices keys cuz it will be sorted by prices
    sorted_menu = sorted(menu_mapping.items())  # sort menu by price which is key in the dictionary
    menu_item = []
    menu_price = []
    for i, j in sorted_menu:
        menu_price.append(i)
        menu_item.append(j)
    menu = [menu_item, menu_price]
    return menu

def edit_menu(menu):
    """I think editing menu is as much important as building menu"""
    import pandas as pd
    print('Current menu is following')
    display(menu)
    ask = int(input('Which row do you want to change 0 to n (n is integer)'))
    item = menu.Items[ask]
    ask_item = input(f'Change the name of {item}')
    ask_price = input(f'Change the price of {ask_item}')
    menu.iloc[ask] = {'Items': ask_item, 'Prices': ask_price}
    print('Your menu is updated')
    return menu

def Build_menu(num):
    """Please input the number items you will sell then following processes will begin soon.
    Don't worry about the difficulty it has very straightforward and intuitive processes"""
    menu = [[], []]  # 0th row is menu, and 1th is price
    for i in range(num):
        product = input("Input item you will sell ")
        price = int(input(f"Input price of '{product}' "))  # prices are int
        menu[0].append(product)
        menu[1].append(price)
    print('Currently added Menu is ', menu)
    ask = input('You want to add more menu? [y]/n ')
    if ask.lower() == 'y':
        ask_num = int(input('How many items you want to add more? '))
        added_menu = Build_menu(ask_num)
        menu[0].extend(added_menu[0])
        menu[1].extend(added_menu[1])
        return menu
    elif ask.lower() == 'n':
        return menu

import pandas as pd
"""For better looking I chose pandas dataframe
Surely if I use a built-function in pandas i can easily sort the data
 but I believe that is not your purpose of this assignment so I took the detour (dictionary)"""
trial = int(input("Input how many items that you will sell "))
my_menu = Build_menu(trial)
my_menu = sort_menu(my_menu)
my_menu = pd.DataFrame({'Items': my_menu[0], 'Prices': my_menu[1]})
display(my_menu)
print("*Important: if you want to eidt or update your menu please call 'edit_menu'")