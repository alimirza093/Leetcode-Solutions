class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        arrive = arrivalTime + delayedTime
        if arrive == 24:
            arrive = 0
        elif arrive > 24:
            arrive -= 24
        return arrive
         