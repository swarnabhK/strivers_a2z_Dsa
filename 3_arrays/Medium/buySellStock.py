# Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and 
# sell on day 5 (price = 6), profit = 6-1 = 5.

#We need to find the maximum positive difference between the stock prices. 

#Approach 1: Brute force, find the profits for each stock, while keepiing a track of the maximum.
# Outer loop: buy stock at ith day, inner loop caluclates whether there is profit in selling that stock in [i+1,n] days. 
#TC : O(N**2)
def buy_sell_stock(prices):
    max_profit = 0
    for i in range(len(prices)):
        buy = prices[i]
        for j in range(i+1,len(prices)):
            sell = prices[j]
            profit = sell-buy
            if(profit>0):
                #means there is profit.
                max_profit = max(profit,max_profit)
    print(max_profit)

prices = [7,1,5,3,6,4]
prices2 = [7,6,5,4,3] #case where there will never be a profit
buy_sell_stock(prices)
buy_sell_stock(prices2)

# appproach 2: 2 pointers. Keep a slow pointer and another fast pointer,if arr[slow]<arr[fast], there is profit, increment fast because there may be other # days with higher profit. in case arr[slow]>arr[fast], make slow = fast, and fast+=1, there can never be a stock with higher profit if we don't increment # slow. Example: [7,1,5,3,6,0,4,9,12]-> if we don't change slow to point to 0, in case 1>0, then we get max profit 12-1 = 11, but if slow is 0,then max profit is 12-0=12. Hence we increment slow to fast, and fast+=1. If we get a smaller stock we will point it to slow.
#TC: O(N)

def buy_sell_stock2(prices):
    if(len(prices)<=1):
        return "Cannot buy and sell stock on the same day"
    max_profit = 0
    slow,fast = 0,1
    while(fast<len(prices)):
        if(prices[slow]<prices[fast]):
            profit = prices[fast]-prices[slow]
            max_profit = max(profit,max_profit)
            fast+=1
        else:
            slow = fast
            fast+=1
    return max_profit

prices3 = [7,1,5,3,6,0,4,9,12]
print(buy_sell_stock2(prices3))

# approach 3: keep track of the current minimum while traversing the array.
# and subtract current minimum with the element. 
# [7,1,5,3,6,0,4,9,12]- > current min for the block [5,3,6] will be 1,so we compute the profit for each element in the else block, and current min for the block [4,9,12] will be 0.
# TC: O(N)

def buy_sell_stock3(prices):
    current_min = float("inf")
    max_profit = 0
    for i in range(len(prices)):
        if(prices[i]<current_min):
            current_min = prices[i]
        else:
            max_profit = max(prices[i]-current_min,max_profit)
    return max_profit

prices4 = [7,1,5,3,6,0,4,9,12]
prices5 = [7,6,5,4,3,1]

print(buy_sell_stock3(prices4))
print(buy_sell_stock3(prices5))
