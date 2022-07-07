def menu(number):
    menu_dict = {
        1: ("Burger", 35.50),
        2: ("Taco", 15.50),
        3: ("Soda", 3.00),
        4: ("Water", 2.25)
    }
    return menu_dict[number]


menu_list = [menu(1), menu(2), menu(3), menu(4)]