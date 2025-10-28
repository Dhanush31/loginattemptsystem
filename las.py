import argparse
import getpass
import time
parser = argparse.ArgumentParser(description="Login attempt system which allows only 3 attempts")
parser.add_argument("--password", type=str, help="Default password", default="admin123") #"--password" is the name of a command-line argument.#It tells Python:#“I will accept a value from the terminal called --password.”
args = parser.parse_args()

correct_password = args.password
attempt = 0

while attempt < 3:
    user_input = getpass.getpass("Enter password: ")#this help to user to enter the password hidden way not show the password

    if user_input == correct_password:
        print("✅ Login success!")
        break
    else:
        attempt += 1
        print("❌ Wrong password!")

        if attempt == 3:
            print("🚫 Too many attempts. Access denied.")
            for i in range(30,0,-1):
                print(f"passed the timer white for {i}",end='\r')
                time.sleep(1)
    


