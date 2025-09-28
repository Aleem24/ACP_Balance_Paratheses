def count_ways_to_make_change(amount, coins):
    
    def count_recursive(remaining, index):
        
        if remaining == 0:
            return 1
        
        if remaining < 0 or index == len(coins):
            return 0
        
        include = count_recursive(remaining - coins[index], index)

        exclude = count_recursive(remaining, index + 1)
    
        return include + exclude
    
    return count_recursive(amount, 0)

amount = int(input("Enter the amount: "))
coins = [1,2,3,4,5]
ways = count_ways_to_make_change(amount, coins)
print(f"Number of ways to divide {amount} using {coins} = {ways}")