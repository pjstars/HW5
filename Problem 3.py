#Author: Pearl John
#Date: 02/15/2024
#Title: Password Simulator 
'''
Description: This program creates a random password that defined a class
PasswordsSimulator that generates random passwords and checks if they 
meet an acceptable critieria. The criteria is special symbols
and not being a dictionary word. The script runs a simulation to generate 
and check passowrds for a specified number of iterations, storing accepted passwords in a list. 
lastly it outputs the list of accepted passwords 
'''


import random
import string

class PasswordSimulator:
    def __init__(self):
        # List to store the accepted passwords
        self.accepted_passwords = []

    def create_password(self, length=10):
        """Generate a random password."""
        letters_and_digits = string.ascii_letters + string.digits
        special_symbols = string.punctuation
        password = ''.join(random.choices(letters_and_digits + special_symbols, k=length))
        return password

    def is_acceptable_password(self, password):
        """Check if the password meets acceptance criteria."""
        # Criteria: includes special symbols and not a dictionary word
        if any(char in string.punctuation for char in password) and password not in ['password', '123456', 'qwerty']:
            return True
        return False

    def simulate(self, num_iterations=40):
        """Simulate generating and checking passwords."""
        for _ in range(num_iterations):
            password = self.create_password()
            if self.is_acceptable_password(password):
                self.accepted_passwords.append(password)
            else:
                # Remove unaccepted passwords from the list
                pass

# Example usage
password_simulator = PasswordSimulator()
password_simulator.simulate()

print("Accepted Passwords:")
for password in password_simulator.accepted_passwords:
    print(password)
