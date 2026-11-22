""" A digit display with a clock function for displaying the time"""
# Imports

import time

# Variables

digits = {
    "0" : ["#####", "#   #", "#   #", "#   #", "#####"],
    "1" : ["  #  ", "  #  ", "  #  ", "  #  ", "  #  "],
    "2" : ["#####", "    #", "#####", "#    ", "#####"],
    "3" : ["#####", "    #", "#####", "    #", "#####"],
    "4" : ["#   #", "#   #", "#####", "    #", "    #"],
    "5" : ["#####", "#    ", "#####", "    #", "#####"],
    "6" : ["#####", "#    ", "#####", "#   #", "#####"],
    "7" : ["#####", "    #", "    #", "    #", "    #"],
    "8" : ["#####", "#   #", "#####", "#   #", "#####"],
    "9" : ["#####", "#   #", "#####", "    #", "#####"],
    ":" : ["     ", "  #  ", "     ", "  #  ", "     "],
    "." : ["     ", "     ", "     ", "     ", "  #  "],
    "-" : ["     ", "     ", "#####", "     ", "     "],
    "+" : ["     ", "  #  ", "#####", "  #  ", "     "],
    " " : ["     ", "     ", "     ", "     ", "     "]
}

def digit_display(characters):
    rows = [""] * 5
    for character in characters:
        if character in digits:
            for i in range(5):
                rows[i] += digits[character][i] + " "
    
    for row in rows:
        print(row)

def hour_min_time():
    print("Ctr+C to end")
    last_time = ""
    try:
        while True:
            current_time = time.strftime("%H:%M", time.localtime())
            if last_time != current_time:
                digit_display(current_time)
                last_time = current_time
                print()

            time.sleep(1)
        
    except KeyboardInterrupt:
        print("\nExiting clock\n")

def digit_user_option():
    while True:
        user_input = input("Time, display input numbers, or exit (1/2/3): ").strip()
        
        if user_input == "1":
            hour_min_time()
            break
            
        elif user_input == "2":
            while True:
                custom_input = input("Input a number to display: ")
                if custom_input and all(char in digits for char in custom_input):
                    digit_display(custom_input)
                    break
                print("Invalid input only accepts numbers")
            break
        
        elif user_input == "3":
            exit()
        else:
            print("Please input in range (1-3)")

while True:
    digit_user_option()