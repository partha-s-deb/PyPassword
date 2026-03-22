from generator import generate_password
from strength import score_password
from breach import check_breach
from utils import print_banner, print_report


def get_yes_no(prompt):
    while True:
        choice = input(prompt + " (y/n): ").strip().lower()
        if choice in ("y", "n"):
            return choice == "y"
        print("  Please enter y or n.")


def get_length():
    while True:
        try:
            length = int(input("  Password length (8-16): ").strip())
            if 8 <= length <= 16:
                return length
            print("  Length must be between 8 and 16.")
        except ValueError:
            print("  Please enter a valid number.")


def main():
    print_banner()

    while True:
        print("\n  MENU")
        print("  1. Generate Password")
        print("  2. Exit")
        print()

        choice = input("  Choose an option: ").strip()

        if choice == "1":
            print()
            length = get_length()
            use_upper   = get_yes_no("  Include uppercase letters?")
            use_lower   = get_yes_no("  Include lowercase letters?")
            use_digits  = get_yes_no("  Include digits?")
            use_symbols = get_yes_no("  Include symbols?")

            try:
                password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
            except ValueError as e:
                print(f"\n  Error: {e}")
                continue

            print("\n  Scoring password...")
            strength_result = score_password(password)

            print("  Checking breach database...")
            breach_result = check_breach(password)

            print()
            print_report(password, strength_result, breach_result)

            again = get_yes_no("\n  Generate another password?")
            if not again:
                print("\n  Goodbye.\n")
                break

        elif choice == "2":
            print("\n  Goodbye.\n")
            break

        else:
            print("  Invalid option. Enter 1 or 2.")


if __name__ == "__main__":
    main()