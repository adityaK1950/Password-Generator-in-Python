import random
import string

print("Welcome to the Random Password Generator 😀")

def main():
    while True:
        length = int(input("Enter the length of your password you want to generate: "))
        lowerD = string.ascii_lowercase
        upperD = string.ascii_uppercase
        digitD = string.digits
        symbolD = string.punctuation

        combine = lowerD + upperD + digitD + symbolD

        x = random.sample(combine, length)

        password = "".join(x)
        print("Password:", password)

        response = input("Do you want to generate another password? (y/n): ")
        if response.lower() != "y":
            break

if __name__ == "__main__":
    main()
