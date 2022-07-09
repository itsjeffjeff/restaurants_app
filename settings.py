#######################~~Questions~~#########################
settings_questions = "1: Update Business Information | 2: View Business Information  | 3: Exit Settings | 4: Shutdown "
table_management_prompt = "1: Assign Table | 2: Assign Order | 3: Print Check | 4: View Table Information " \
                          "|5: Remove Table | 6: Edit Settings"

#######################~~Table Dictionary~~#########################
tables = {
    1: {
        # "name": 'Sides, Jeff',
        # "VIP_Status": True,
        # "Reservation": "17:30",
        # 'Order': [('Burger', 35.5), ('Water', 2.25)],
        # "Split/Bill: $XX.XX"
        # "Tip: $XX:XX"
    },
    2: {},
    3: {},
    4: {},
    5: {},
}


#######################~~Menu Dictionary~~#########################
def menu(number):
    menu_dict = {
        1: ("Burger", 35.50),
        2: ("Taco", 15.50),
        3: ("Soda", 3.00),
        4: ("Water", 2.25)
    }
    return menu_dict[number]


menu_list = [menu(1), menu(2), menu(3), menu(4)]


#######################~~Functions~~#########################
def update_business(business):
    try:
        updating = True
        while updating is True:
            print('[1] Change name \n[2] Change Address \n[3] Change Phone Number \n[4] Change Hours\n[5] Go Back')
            prompt = int(input("What would you like to update? >>"))
            if prompt == 1:
                business.name = input("New Name: ")
            elif prompt == 2:
                business.address = input("New Address: ")
            elif prompt == 3:
                business.phone_number = input("New Phone Number: ")
            elif prompt == 4:
                business.open = input("New Open Time: ")
                business.closed = input("New Close Time: ")
            elif prompt == 5:
                break
    except ValueError:
        print("\n***Invalid Entry***\n")
        update_business(business)


def program():
    # Pull in Business Data
    build = Restaurant("No Name", "No Address", "No Phone Number", "No Hours", "No Hours")
    return build


def table_information():
    t_number = int(input("Table Number: "))
    t_name = str(input("Guest Name: ").title())
    t_reservation = str(input("Reservation Time: "))
    if t_reservation == " ":
        t_reservation = None
    else:
        t_reservation = t_reservation[:2] + ":" + t_reservation[2:]
    t_status = input("True/False: ").title()
    if t_status == "True":
        t_status = True
    else:
        t_status = False
    return t_number, t_name, t_reservation, t_status


def table_order():
    t_number = int(input("Table Number: "))
    try:
        while True:
            print('[1] Add \n[2] Remove \n[3] View Order |\n[4] Go Back')
            prompt = int(input("Add/Remove item to Order >>"))
            if prompt == 1:
                print(menu_list)
                menu_item = int(input("Add item >>"))
                if menu_item == 1:
                    tables[t_number]['Order'].append(menu_list[0])
                elif menu_item == 2:
                    tables[t_number]['Order'].append(menu_list[1])
                elif menu_item == 3:
                    tables[t_number]['Order'].append(menu_list[2])
                elif menu_item == 4:
                    tables[t_number]['Order'].append(menu_list[3])
            elif prompt == 2:
                removed = tables[t_number]['Order'].pop()
                print(f"{removed} was removed")
            elif prompt == 3:
                print(tables[t_number])
            elif prompt == 4:
                break

    except ValueError:
        print("\n***Invalid Entry***\n")
        update_business(business)


def shutdown():
    quit()


#######################~~Classes~~#########################
class Restaurant:

    def __init__(self, name, address, phone_number, opening, close):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.open = opening
        self.closed = close

    @staticmethod
    def assign_table(table_number, name, reservation=None, vip_status=False):
        if reservation is None and tables[table_number] != tables[table_number].clear():
            tables[table_number]["Name"] = name
            tables[table_number]["VIP_Status"] = vip_status
            tables[table_number]['Order'] = []
        else:
            tables[table_number]["Name"] = name
            tables[table_number]["Reservation Time"] = reservation
            tables[table_number]["VIP_Status"] = vip_status
            tables[table_number]['Order'] = []

    @staticmethod
    def assign_order(table_number, *orders):
        lst_of_order = []

        for order in orders:
            lst_of_order.append(order)
            tables[table_number]['Order'] = lst_of_order

    @staticmethod
    def remove_table(table_number):
        tables[table_number].clear()

    @staticmethod
    def calculate_bill(table_number, split=None):
        total = 0
        if split <= 1:
            order = [tables[table_number]["Order"]]
            for o in order:
                for price in o:
                    total += price[1]
            tables[table_number]['Bill'] = total
            return total, 1
        else:
            order = tables[table_number]['Order']
            for o in order:
                total += o[1]
            tables[table_number]['Bill'] = total
            split_total = total / split
            return split_total, split

    def __repr__(self):
        return f"Business Name: {self.name} | Address: {self.address} Number: {self.phone_number} | " \
               f"Hours: {self.open} - {self.closed}"