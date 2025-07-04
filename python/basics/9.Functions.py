# 9. Functions
# Definition: Functions are reusable blocks of code.
# Scenario: You create a function that calculates the total fare based on distance.:
# Example: A function to calculate fare based on distance


def calculate_fare(distance): #function definition , distance is a parameter
    return distance * 12

print("Total fare: ₹", calculate_fare(10))#function call, 10 is an argument
