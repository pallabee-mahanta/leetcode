class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # solve it the DP way
        combinations = [0] * (amount + 1)
        combinations[0] = 1

        for coin in coins:
            for i in range(coin, len(combinations)):
                combinations[i] += combinations[i - coin]

        return combinations[-1]

# Example usage:
sol = Solution()
amount = 5
coins = [1, 2, 5]
print(sol.change(amount, coins))  # Output: 4