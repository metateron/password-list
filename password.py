import secrets
import hashlib
import time
import time
import os
from colorama import init, Fore, Style
from colorama import init, Fore, Back, Style

init(autoreset=True)

def clear_console():
   
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_color_banner(text):
    banner_length = len(text) + 4
    colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
    
    for i in range(banner_length):
        clear_console()  
        color_index = (i // 2) % len(colors) 
        print(colors[color_index] + '*' * banner_length)  
        print(colors[color_index] + '* ' + Style.RESET_ALL + text + ' ' + colors[color_index] + '*') 
        print(colors[color_index] + '*' * banner_length)  
        time.sleep(0.2)  

def main():
    title = "METATERON"
    animated_color_banner(title)

if __name__ == "__main__":
    main()

chars_alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
chars_digits = '1234567890'
chars_combined = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-='
length = 12

def generate_password(chars):
    return ''.join(secrets.choice(chars) for _ in range(length))

def main():
    while True:
        print(Fore.GREEN + "List password type :")
        print(Fore.BLUE + "1. Alphabetical")
        print(Fore.BLUE + "2. Numerical")
        print(Fore.BLUE + "3. Combined (Alpha + Numeric + Special Characters)")
        print(Fore.RED +  "4. Exit")

        choice = input(Fore.YELLOW + "Enter (1/2/3/4): ")
        
        if choice == '1':
            print("Generating Alphabetical Passwords. Press Ctrl+C to stop.")
            try:
                while True:
                    password = generate_password(chars_alpha)
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()
                    print(Fore.BLUE + "Generated Alphabetical Password:",Fore.GREEN + password)
                    print(Fore.CYAN + "Hashed Password:",Fore.GREEN +  hashed_password)

            except KeyboardInterrupt:
                print(Fore.GREEN + "\nAlphabetical password generation stopped.")

        elif choice == '2':
            print("Generating Numerical Passwords. Press Ctrl+C to stop.")
            try:
                while True:
                    password = generate_password(chars_digits)
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()
                    print(Fore.BLUE + "Generated Numerical Password:",Fore.GREEN + password)
                    print(Fore.CYAN + "Hashed Password:",Fore.GREEN + hashed_password)

            except KeyboardInterrupt:
                print("\nNumerical password generation stopped.")

        elif choice == '3':
            print("Generating Combined Passwords. Press Ctrl+C to stop.")
            try:
                while True:
                    password = generate_password(chars_combined)
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()
                    print(Fore.BLUE + "Generated Combined Password:",Fore.GREEN +  password)
                    print(Fore.CYAN + "Hashed Password:",Fore.GREEN + hashed_password)

            except KeyboardInterrupt:
                print("\nCombined password generation stopped.")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()