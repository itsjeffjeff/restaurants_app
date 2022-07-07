from functions.modules import *


def run_app():
    business = program()
    run = True
    while run is True:
        # print("\n")
        print(prompt_question)
        prompt = int(input("What would you like to do ?"))
        if prompt == 1:
            print('\n')
            update_business(business)
            print('\n')
        elif prompt == 2:
            print('\n')
            print(business)
            print('\n')
        elif prompt == 3:
            run = False
        elif prompt < 1 or prompt > 3:
            print("Invalid Entry")
            continue
