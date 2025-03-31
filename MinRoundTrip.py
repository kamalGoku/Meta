'''
You are given 2 arrays departure and return where departure[i] and returns[i] are ticket prices for departing and returning flights
on ith day respectively
You want to minimize your cost by choosing a single day to buy a delarture flight and choosing a different day in future to
buy a returning flight
Return mimimum cost you can achive from a single round trip flight

Example:

departure = [1,2,3,4]
returns = [4,3,2,1]
Output: 2
Buy a departure flight on day0(price=1) and buy a return ticket on day3(price=1) cost=1+1 = 2

'''
import sys

def minRoundTrip(departure, returns) -> int:
    minCost = sys.maxsize
    minDeparture = departure[0]
    for i in range(1,len(departure)):
        minCost = min(minCost, returns[i]+minDeparture)
        minDeparture = min(minDeparture, departure[i])
    return minCost

#departure = [1,2,3,4]
#returns = [4,3,2,1]
departure = [10, 9, 8, 7, 6]
returns = [6, 7, 8, 9, 10]
print("Min Cost = ", minRoundTrip(departure, returns))
