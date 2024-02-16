#Author: Pearl John
#Date: 02/15/2024
#Title: Non-disparate DATA WAREHOUSING
#Descritption: The program defines a 'DataCollector' class that generates and stores sample user data, allowing for searched based on user attributes such as state or salesperson.

import random
import string

class DataCollector:
    def __init__(self):
        #dictionary to store the user data
        self.data_store = {}

    def generate_random_string(self, length=8):
        """Generate a random string of letters and digits."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def generate_user_data(self):
        """Generate sample user data."""
        #Generating random data for various user attribute 
        username = self.generate_random_string()
        password = self.generate_random_string()
        birthdate = f"{random.randint(1950, 2000)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
        address = f"{random.randint(100, 999)} {self.generate_random_string()} St"
        social_security_number = f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"
        product_purchased = {
            f"ID-{self.generate_random_string(6)}": {
                "quantity": random.randint(1, 10),
                "date_ordered": f"{random.randint(1, 12)}/{random.randint(1, 28)}/{random.randint(2010, 2023)}",
                "region": random.choice(["North", "South", "East", "West"])
            }
        }
        salesperson = self.generate_random_string()
        state = random.choice(["CA", "NY", "TX", "FL"])  # Add state attribute
        return {
            "username": username,
            "password": password,
            "birthdate": birthdate,
            "address": address,
            "social_security_number": social_security_number,
            "product_purchased": product_purchased,
            "salesperson": salesperson,
            #Including state attribute
            "state": state 
        }

     #Increased sample size
    def collect_data(self, num_records=50): 
        """Generate and collect sample user data."""
         #Generating and collecting user data
        for _ in range(num_records):
            user_id = self.generate_random_string()
            self.data_store[user_id] = self.generate_user_data()

    def search_by_state(self, state):
        """Search for users in a certain state."""
        results = []
        for user_id, data in self.data_store.items():
             # Checking the state attribute
            if data['state'] == state: 
                results.append((user_id, data))
        return results

    def search_by_salesperson(self, salesperson):
        """Search for users handled by a certain salesperson."""
        results = []
        for user_id, data in self.data_store.items():
            if data['salesperson'] == salesperson:
                results.append((user_id, data))
        return results

# Example usage
data_collector = DataCollector()
data_collector.collect_data(num_records=5)  # Increased sample size

# Print some sample user data
print("Sample User Data:")
for user_id, data in data_collector.data_store.items():
    print(f"User ID: {user_id}, Data: {data}")

# Search for users in a certain state
state_search_results = data_collector.search_by_state("CA")
print("\nUsers in California:")
for user_id, data in state_search_results:
    print(f"User ID: {user_id}, Data: {data}")

# Search for users handled by a certain salesperson
salesperson_search_results = data_collector.search_by_salesperson("JohnDoe")
print("\nUsers handled by John Doe:")
for user_id, data in salesperson_search_results:
    print(f"User ID: {user_id}, Data: {data}")



