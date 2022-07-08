from functions.modules import program

business = program()


def run_app():
    run = True
    while run is True:
        # print("\n")
        from functions.modules import settings_questions
        print(settings_questions)
        prompt = int(input("What would you like to do ?"))
        if prompt == 1:
            from functions.modules import update_business
            print('\n')
            update_business(business)
            print('\n')
        elif prompt == 2:
            print('\n')
            print(business)
            print('\n')
        elif prompt == 3:
            print('\n')
            run_application()
            print('\n')
        elif prompt == 4:
            run = False
        elif prompt < 1 or prompt > 3:
            print("Invalid Entry")
            continue


def run_application():
    running = True
    while running is True:
        from functions.modules import table_management
        from functions.modules import tables
        print(table_management)
        prompt = int(input("What would you like to do ?"))
        if prompt == 1:
            t_number = int(input("Table Number: "))
            t_name = str(input("Guest Name: "))
            reservation_time = str(input("Reservation Time: "))
            if reservation_time == " ":
                reservation_time = None
            t_status = input("True/False").title()
            if t_status == "True":
                t_status = True
            else:
                t_status = False
            business.assign_table(t_number, t_name, reservation_time, t_status)

        elif prompt == 4:
            t_number = int(input("Table Number: "))
            print(tables[t_number])
