import random
import string

def generate_password(length):
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(characters)
    password = ''.join(random.choice(characters, k=length))
    return password

def main():
   
    length = int(input("Enter the desired  password length : ")) 
    password = generate_password(length)
    print("Your password is: {password}") 
        
if __name__ == "__main__":
    main()
