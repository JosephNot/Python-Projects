"""Resistance calculator for tempeature's effect on resistance for a positive effect"""

# Variables

user_list = []
run = True

def calculate_base_resistance(final_resistance, temperature_effect, temperature_range):
    base_resistance = final_resistance / (1 + (temperature_effect * temperature_range))
    return base_resistance

def calculate_final_resistance(base_resistance, temperature_effect, temperature_range):
    final_resistance = base_resistance * (1 + (temperature_effect * temperature_range))
    return final_resistance

def calculate_temperature_range(base_resistance, final_resistance, temperature_effect):
    resistance_ratio = final_resistance / base_resistance
    temperature_range = (resistance_ratio - 1) / temperature_effect
    return temperature_range

def calculate_temperature_effect(base_resistance, final_resistance, temperature_range):
    resistance_ratio = final_resistance / base_resistance
    temperature_effect = (resistance_ratio - 1) / temperature_range
    return temperature_effect

def user_add_list(base_resistance, final_resistance, temperature_effect, temperature_range, result):
    global user_list

    user_result = {
    "base_resistance" : base_resistance,
    "final_resistance" : final_resistance,
    "temperature_effect" : temperature_effect,
    "temperature_range" : temperature_range,
    "result" : result
    }

    user_list.append(user_result)

def get_user_calculation():
    global run

    print("A resistance calculator for temperature,\nbut only works for positive gradient")
    print("Put in a value or press Enter to calcuate unkown:")
    try:
        base_resistance = input("Base resistance: ") or None
        final_resistance = input("Final resistance: ") or None
        temperature_effect = input("Temperature effect: ") or None
        temperature_range = input("Temperature range: ") or None

    except (EOFError, KeyboardInterrupt):
        print("\nExit program")
        run = False
        return


    try:
        # Casting
        if base_resistance is not None:
            base_resistance = float(base_resistance)

        if final_resistance is not None:
            final_resistance = float(final_resistance)

        if temperature_effect is not None:
            temperature_effect = float(temperature_effect)

        if temperature_range is not None:
            temperature_range = float(temperature_range)

        # Check

        if temperature_effect is not None and temperature_effect <= 0:
            print("This calculator only supports positive temperature coefficient (PTC)")
            return 

        if base_resistance is not None and base_resistance <= 0:
            print("Base resistance must be positive")
            return

        if final_resistance is not None and final_resistance <= 0:
            print("Final resistance must be positive")
            return

        # Calculation

        if base_resistance is None:
            result = calculate_base_resistance(final_resistance, temperature_effect, temperature_range)
        
        elif final_resistance is None:
            result = calculate_final_resistance(base_resistance, temperature_effect, temperature_range)
        
        elif temperature_range is None:
            result = calculate_temperature_range(base_resistance, final_resistance, temperature_effect)
        
        elif temperature_effect is None:
            result = calculate_temperature_effect(base_resistance, final_resistance, temperature_range)
        
        else:
            print("One value must be blank to calculate")
            return

        if result <= 0:
            print("Result is not physicaly possible (R < 0)")
            return
        
        print(result)
        user_add_list(base_resistance, final_resistance, temperature_effect, temperature_range, result)

    except TypeError:
        print("Error as one value can only be blank")
        return

    except ValueError:
        print("Error as must be numberical")
        return
    
    except ZeroDivisionError:
        print("Error as not divisible by zero")
        return


def user_answers():
    for index, user_result in enumerate(user_list):
        print(f"{index + 1}:")
        for j, (key, value) in enumerate(user_result.items()):
            print(f"{key}: {value}")

        print()

def user_option():
    global run

    get_user_calculation()
    if not run:
        return

    while True:
        user_input = input("End, continue or print answers (0/1/2): ")
        if user_input == "0":
            run = False
            break

        elif user_input == "1":
            break

        elif user_input == "2":
            user_answers()
            break

        else:
            print("Unknown input, enter between (0-2)")   


while run:
    user_option()
    print()
