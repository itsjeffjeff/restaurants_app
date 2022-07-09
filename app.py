from settings import program

business = program()


def run_app():
    run = True
    while run is True:
        try:
            from settings import settings_questions
            print(settings_questions)
            prompt = int(input("What would you like to do ?"))
            if prompt == 1:
                from settings import update_business
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
                from settings import shutdown
                shutdown()
        except ValueError:
            print("Invalid Entry")


def run_application():
    running = True
    while running is True:
        from settings import table_management_prompt
        from settings import tables
        from settings import table_information
        from settings import table_order
        print("\n", table_management_prompt, "\n")
        prompt = int(input("What would you like to do ?"))
        print("\n")
        if prompt == 1:  # Assign Table
            t_number, t_name, t_reservation, t_status = table_information()
            business.assign_table(t_number, t_name, t_reservation, t_status)
        elif prompt == 2: # Assign Order
            table_order()
        elif prompt == 3:
            t_number = int(input("Table Number: "))
            t_split = int(input("Split Number: "))
            business.calculate_bill(t_number, t_split)
        elif prompt == 4:
            t_number = int(input("Table Number: "))
            print(tables[t_number])
        elif prompt == 6:
            run_app()