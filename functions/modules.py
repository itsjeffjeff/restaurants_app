from functions.table_dict import tables
from functions.menus import menu_list

#######################~~Questions~~#########################
prompt_question = "1: Update Business Information | 2: View Business Information  | 3: Quit"


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
        if split is None:
            order = [tables[table_number]["Order"]]
            for o in order:
                for price in o:
                    total += price[1]
            tables[table_number]['Bill'] = total
            return total, None
        else:
            order = tables[table_number]['Order']
            for o in order:
                total += o[1]
            tables[table_number]['Bill'] = total
            split_total = total / split
            return split_total, split

    def __repr__(self):
        return f"Business Name: {self.name} | Address: {self.address} Number: {self.phone_number} | " \
               f"Open: {self.open} Closed: {self.closed}"
