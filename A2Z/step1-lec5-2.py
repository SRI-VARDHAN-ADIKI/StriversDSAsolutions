#User function Template for python3

class Solution:
    def __init__(self):
        self.i = 1  # Initialize i as an instance variable

    def printGfg(self, n):
        # Code here
        if self.i <= n:
            print("GFG", end=" ")
            self.i += 1
            self.printGfg(n)  # Correct the recursive call to use self
        else:
            return

