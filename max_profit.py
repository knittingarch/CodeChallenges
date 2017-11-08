def get_max_profit_final(prices):
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')    
    min_price = prices[0]
    max_profit = prices[1] - prices[0]
    for index, current_price in enumerate(prices):
        if index == 0:
            continue
        potential_profit = current_price - min_price
        print potential_profit
        max_profit = max(max_profit, potential_profit)
        print min_price, current_price
        min_price = min(current_price, min_price)
        print max_profit
        print "-------"
    return max_profit

# My attempt at the final solution

def get_max_profit(prices):
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')
    min_price = prices[0]
    max_profit = prices[1] - prices[0]
    print min_price, max_profit
    for current_price in prices:
        min_price = min(current_price, min_price)
        print min_price, current_price
        potential_profit = current_price - min_price
        print potential_profit
        if potential_profit < max_profit:
            max_profit = potential_profit
        print max_profit
        print "-------"
    return max_profit

# Works for varying and stagnant prices but not dropping prices

def get_max_profit(prices):
    max_profit = 0
    min_price = prices[0]
    for current_price in prices:
        min_price = min(min_price, current_price)
        print min_price, current_price
        potential_profit = current_price - min_price
        print potential_profit
        max_profit = max(max_profit, potential_profit)
        print max_profit
        print "-------"
    return max_profit


# Better, but still O(n2).

def get_max_profit(prices):
    max_profit = 0
    for earlier_time, earlier_price in enumerate(prices):
        for later_price in prices[earlier_time+1:]:
            potential_profit = later_price - earlier_price
            print potential_profit, max_profit
            max_profit = max(max_profit, potential_profit)
            print max_profit
            print "-------"
    return max_profit



# This reports negagtive profits and is O(n2).  No bueno.

def get_max_profit2(prices):
    max_profit = 0
    for outer_time in xrange(len(prices)):
        for inner_time in xrange(len(prices)):
            print outer_time, inner_time
            earlier_time = min(outer_time, inner_time)
            later_time = max(outer_time, inner_time)
            print earlier_time, later_time
            earlier_price = prices[earlier_time]
            later_price = prices[later_time]
            print earlier_price, later_price
            potential_profit = later_price - earlier_price
            print potential_profit, max_profit
            max_profit = max(max_profit, potential_profit)
            print max_profit
            print "-------"
    return max_profit
