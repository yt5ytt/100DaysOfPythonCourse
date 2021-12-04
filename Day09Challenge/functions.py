def find_highest_bidder(all_bidders):
    highest_bidder = ""
    highest_bid = 0
    for key in all_bidders:
        if all_bidders[key] > highest_bid:
            highest_bidder = key
            highest_bid = all_bidders[key]

    from clear import clear
    clear()
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")