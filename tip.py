# Dollars to Float converting function.
def dollars_to_float(d):
    return float(d.strip("$"))

# Percentage to Float converting function.
def percent_to_float(p):
    return float(float(p.strip("%"))/100)

# Tip calculator function.
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

main()