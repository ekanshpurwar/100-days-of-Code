
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
bidders = {}

while True:

    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if other_bidders == "yes":
        continue
    else:
        max_bid = 0
        for key in bidders:
            if bidders[key] > max_bid:
                max_bid = bidders[key]
                winner_name = key
        print(f"The winner is {winner_name} with a bid of ${max_bid}")
        break