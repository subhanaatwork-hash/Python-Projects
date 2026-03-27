def main_menu():
    print("\n====== MULTIPURPOSE CONVERTER ======")
    print("1. Temperature Converter")
    print("2. Length Converter")
    print("3. Weight Converter")
    print("4. Speed Converter")
    print("5. Exit")
    print("====================================")

# ---------------- TEMPERATURE ----------------
def temperature_converter():
    while True:
        print("\n--- TEMPERATURE CONVERTER ---")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")

        choice = input("Enter choice: ")
        temp = float(input("Enter temperature value: "))

        if choice == "1":
            print("Fahrenheit =", int((temp * 9/5) + 32))
        elif choice == "2":
            print("Celsius =", int((temp - 32) * 5/9))
        elif choice == "3":
            print("Kelvin =", int(temp + 273.15))
        elif choice == "4":
            print("Celsius =", int(temp - 273.15))
        else:
            print("Invalid option!")

        again = input("Convert another temperature? (y/n): ").lower()
        if again != "y":
            break


# ---------------- LENGTH ----------------
def length_converter():
    while True:
        print("\n--- LENGTH CONVERTER ---")
        print("1. km to m")
        print("2. m to cm")
        print("3. cm to inches")
        print("4. inches to feet")

        choice = input("Enter choice: ")
        value = float(input("Enter value: "))

        if choice == "1":
            print("Meters =", int(value * 1000))
        elif choice == "2":
            print("Centimeters =", int(value * 100))
        elif choice == "3":
            print("Inches =", int(value / 2.54))
        elif choice == "4":
            print("Feet =", int(value / 12))
        else:
            print("Invalid option!")

        again = input("Convert another length? (y/n): ").lower()
        if again != "y":
            break


# ---------------- WEIGHT ----------------
def weight_converter():
    while True:
        print("\n--- WEIGHT CONVERTER ---")
        print("1. kg to grams")
        print("2. grams to kg")
        print("3. kg to pounds")
        print("4. pounds to kg")

        choice = input("Enter choice: ")
        value = float(input("Enter value: "))

        if choice == "1":
            print("Grams =", int(value * 1000))
        elif choice == "2":
            print("Kilograms =", int(value / 1000))
        elif choice == "3":
            print("Pounds =", int(value * 2.20462))
        elif choice == "4":
            print("Kilograms =", int(value / 2.20462))
        else:
            print("Invalid option!")

        again = input("Convert another weight? (y/n): ").lower()
        if again != "y":
            break


# ---------------- SPEED ----------------
def speed_converter():
    while True:
        print("\n--- SPEED CONVERTER ---")
        print("1. km/h to m/s")
        print("2. m/s to km/h")
        print("3. km/h to mph")

        choice = input("Enter choice: ")
        value = float(input("Enter value: "))

        if choice == "1":
            print("m/s =", int(value / 3.6))
        elif choice == "2":
            print("km/h =", int(value * 3.6))
        elif choice == "3":
            print("mph =", int(value * 0.621371))
        else:
            print("Invalid option!")

        again = input("Convert another speed? (y/n): ").lower()
        if again != "y":
            break

# ---------------- MAIN PROGRAM LOOP ----------------
while True:
    main_menu()
    option = input("Choose an option: ")

    if option == "1":
        temperature_converter()
    elif option == "2":
        length_converter()
    elif option == "3":
        weight_converter()
    elif option == "4":
        speed_converter()
    elif option == "5":
        print("Goodbye! Thanks for using the converter.")
        break
    else:
        print("Invalid choice! Try again.")

