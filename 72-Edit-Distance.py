
\\\
This recursive solution calculates the minimum edit distance between two words by exploring all possible operations: insert, delete, and replace. 
The function recursively reduces the problem size by processing one character at a time, either matching or transforming it, and accumulates the cost of operations.
\\\

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        # Define a recursive function to calculate edit distance
        def calculateDistance(index1: int, index2: int) -> int:
            if (index1, index2) in dp:
                return dp[(index1, index2)]
            # Base case: if the first word is exhausted, return the length of the remaining second word
            if index1 == len(word1):
                return len(word2) - index2

            # Base case: if the second word is exhausted, return the length of the remaining first word
            if index2 == len(word2):
                return len(word1) - index1

            # If characters match, move to the next pair of characters
            if word1[index1] == word2[index2]:
                dp[(index1, index2)] = calculateDistance(index1 + 1, index2 + 1)
                return dp[(index1, index2)]

            # Calculate the cost of insert, delete, and replace operations
            insertCost = 1 + calculateDistance(index1, index2 + 1)
            deleteCost = 1 + calculateDistance(index1 + 1, index2)
            replaceCost = 1 + calculateDistance(index1 + 1, index2 + 1)
            dp[(index1, index2)] = min(insertCost, deleteCost, replaceCost)
            # Return the minimum cost among the three operations
            return min(insertCost, deleteCost, replaceCost)

        # Start the recursion from the beginning of both words
        return calculateDistance(0, 0)
