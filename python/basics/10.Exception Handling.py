# 12. Exception Handling (try-except)
# Definition: It handles errors without crashing the program.

# Scenario: A payment gateway handles wrong card input:


try:
    a = 10/0
    print(a)
except:
    print("Can not divisible by Zero.")
