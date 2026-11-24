"""Resistance calculator for tempeature effect on resistance"""

# Variables

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

def get_user_calculation():
    print("Put in a value or press Enter if unknown:")
    try:
        base_resistance = input("Base resistance: ") or None
        final_resistance = input("Final resistance: ") or None
        temperature_effect = input("Temperature effect: ") or None
        temperature_range = input("Temperature range: ") or None

    except Exception:
        print("Input not valid")
        return

    try:
        if base_resistance is None:
            final_resistance, temperature_effect, temperature_range = float(final_resistance), float(temperature_effect), float(temperature_range)
            result = calculate_base_resistance(final_resistance, temperature_effect, temperature_range)
            print(result)

        elif final_resistance is None:
            base_resistance, temperature_effect, temperature_range = float(base_resistance), float(temperature_effect), float(temperature_range)
            result = calculate_final_resistance(base_resistance, temperature_effect, temperature_range)
            print(result)

        elif temperature_range is None:
            base_resistance, final_resistance, temperature_effect = float(base_resistance), float(final_resistance), float(temperature_effect)
            result = calculate_temperature_range(base_resistance, final_resistance, temperature_effect)
            print(result)

        elif temperature_effect is None:
            base_resistance, final_resistance, temperature_range = float(base_resistance), float(final_resistance), float(temperature_range)
            result = calculate_temperature_effect(base_resistance, final_resistance, temperature_range)
            print(result)
        
        else:
            print("One value must be blank to calculate")

    except TypeError:
        print("Error as one value can only be blank")

    except ValueError:
        print("Error as must be numberical")
    
    except ZeroDivisionError:
        print("Error as not divisible by zero")


while run:
    get_user_calculation()
    run_program = input("End program or continue (0/1): ")
    print()
    if run_program == "0":
        run = False
