import math     # Importing the math module as instructed

# Asking user to decide on the financial calculator they would like to use. Using '\n' for line break as looks neater
calc_type = input("\nChoose either 'investment' or 'bond' from the menu below to proceed: \n\ninvestment - to calculate the amount of interest you'll earn on interest \nbond - to calculate the amount you'll have to pay on a home loan\n\nPlease type your answer in here: " ).upper()

# If user has typed 'Investment' the below control structure executes
if calc_type == "INVESTMENT":

    # Variables saved by user inputting their answer
    initial_deposit = float(input("How much money are you going to deposit?: "))
    interest_rate = float(input("What is the interest rate?: "))/100    # Dividing by 100 to get their integer saved as a percentage
    period = float(input("How many years are you planning to invest?: " ))
    interest = input("Would you like to have 'simple' or 'compound' interest?: ").upper()

    # The 'simple' interest calculation executes below if user chooses 'simple'
    if interest == "SIMPLE":
        simple_calc = round(initial_deposit*(1+interest_rate*period),2)
        print(f"\nYour total investment using the 'simple' interest investment calculation will be R{simple_calc}")

    # The 'compound' interest calculation executes below if user chooses 'compound'
    elif interest == "COMPOUND":
        compound_calc = initial_deposit*math.pow((1+interest_rate),period)
        print(f"\nYour total investment using the 'compound' interest investment calculation will be R{compound_calc}")

# If user has typed 'Bond' the below control structure executes
elif calc_type == "BOND":
    present_value = float(input("What is the present value of the house?: "))
    interest_rate_monthly = float(input("What is the interest rate?: "))/100/12 # Divided by 12 to get monthly interest rate
    months = float(input("How many months do you plan to take to pay off the bond?: "))
    repayment_calc = (interest_rate_monthly*present_value)/(1-(1+interest_rate_monthly)**(-months))
    print(f"\nYour monthly repayments on your bond will be R{repayment_calc}")

# If user has entered neither 'investment' or 'bond' the program will prompt the user for a valid entry
else:
    print("Please enter a valid choice of financial calculator, either type 'investment' or 'bond'")