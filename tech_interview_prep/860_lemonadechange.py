# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# Note that you do not have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

class Solution:
    def lemonadeChange(self, bills) -> bool:
        #if 5$ bill,keep it
        # if 10$ bill, if you have 5$ bill, give it as change, if not return false
        # if 20$ bill, check if you have a 10$ bill and 5$ bill, if not check if you have 
        # 3 5$ bills, if not return False
        fives,tens = 0,0
        for bill in bills:
            if bill==5:
                fives+=1
            elif bill==10:
                if fives==0:
                    return False
                fives-=1
                tens+=1
            else:
                if tens>0 and fives>0:
                    tens-=1
                    fives-=1
                elif fives>=3:
                    fives-=3
                else:
                    return False
        return True
                