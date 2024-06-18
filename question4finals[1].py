def show_menu():
    print("Measurement Converter Menu:")
    print("1. Millimeter to Centimeter")
    print("2. Centimeter to Meter")
    print("3. Meter to Kilometer")
    print("4. Feet to Meter")
    print("5. Inch to Centimeter")

def convert_mm_to_cm(mm):
    return mm / 10

def convert_cm_to_m(cm):
    return cm / 100

def convert_m_to_km(m):
    return m / 1000

def convert_ft_to_m(ft):
    return ft * 0.3048

def convert_in_to_cm(inch):
    return inch * 2.54

def main():
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        mm = float(input("Enter length in millimeters: "))
        cm = convert_mm_to_cm(mm)
        print(f"{mm} mm is equal to {cm} cm")
    elif choice == '2':
        cm = float(input("Enter length in centimeters: "))
        m = convert_cm_to_m(cm)
        print(f"{cm} cm is equal to {m} m")
    elif choice == '3':
        m = float(input("Enter length in meters: "))
        km = convert_m_to_km(m)
        print(f"{m} m is equal to {km} km")
    elif choice == '4':
        ft = float(input("Enter length in feet: "))
        m = convert_ft_to_m(ft)
        print(f"{ft} ft is equal to {m} m")
    elif choice == '5':
        inch = float(input("Enter length in inches: "))
        cm = convert_in_to_cm(inch)
        print(f"{inch} inches is equal to {cm} cm")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()