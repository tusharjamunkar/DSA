"""
0121. Best Time to Buy and Sell Stock
Difficulty: Easy
Topic: Sliding Window / Two Pointers / Dynamic Programming
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve
any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Optimal Sliding Window / Two-Pointer Approach:
        
        Algorithmic Intuition:
        - Maintain `left` as the candidate buying day and `right` as the candidate selling day.
        - Initialize `left = 0`, `right = 1`.
        - As `right` sweeps forward:
          - If `prices[left] < prices[right]`:
            - A positive transaction exists: `profit = prices[right] - prices[left]`.
            - Update `max_profit = max(max_profit, profit)`.
          - Else (`prices[right] <= prices[left]`):
            - We discovered a cheaper buying opportunity at `right`!
            - Any future day `k > right` paired with `prices[right]` will yield a strictly
              larger profit than paired with `prices[left]`.
            - Slide the buying window: `left = right`.
          - Advance `right += 1`.
        
        Time Complexity:  O(n) - Single pass through the array.
        Space Complexity: O(1) - Constant auxiliary space.
        """
        if len(prices) < 2:
            return 0

        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit
            else:
                left = right
            right += 1

        return max_profit

    def maxProfitRunningMin(self, prices: List[int]) -> int:
        """
        Single-Pass Running Minimum Approach (Kadane Variant):
        
        - Keep track of the minimum price observed so far (`min_price`).
        - For each day's price, compute potential profit = price - min_price.
        - Update max_profit accordingly.
        
        Time Complexity:  O(n) - Single pass.
        Space Complexity: O(1) - Two scalar variables.
        """
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


# ==========================================
# Unit Tests & Verification
# ==========================================
def test_best_time_to_buy_and_sell_stock():
    sol = Solution()

    # Test Case 1: Standard peak and valley
    p1 = [7, 1, 5, 3, 6, 4]
    assert sol.maxProfit(p1) == 5
    assert sol.maxProfitRunningMin(p1) == 5

    # Test Case 2: Monotonically decreasing (no profit possible)
    p2 = [7, 6, 4, 3, 1]
    assert sol.maxProfit(p2) == 0
    assert sol.maxProfitRunningMin(p2) == 0

    # Test Case 3: Monotonically increasing (max profit between first and last)
    p3 = [1, 2, 3, 4, 5]
    assert sol.maxProfit(p3) == 4
    assert sol.maxProfitRunningMin(p3) == 4

    # Test Case 4: Single element array (cannot buy and sell)
    p4 = [5]
    assert sol.maxProfit(p4) == 0
    assert sol.maxProfitRunningMin(p4) == 0

    # Test Case 5: Flat prices
    p5 = [3, 3, 3, 3]
    assert sol.maxProfit(p5) == 0
    assert sol.maxProfitRunningMin(p5) == 0

    # Test Case 6: Buy on lowest dip after a high peak
    p6 = [3, 8, 1, 4]
    assert sol.maxProfit(p6) == 5  # 8 - 3 = 5 > 4 - 1 = 3
    assert sol.maxProfitRunningMin(p6) == 5

    # Test Case 7: Late monster gain
    p7 = [10, 9, 2, 5, 3, 7, 101, 18]
    assert sol.maxProfit(p7) == 99  # 101 - 2 = 99
    assert sol.maxProfitRunningMin(p7) == 99


if __name__ == "__main__":
    test_best_time_to_buy_and_sell_stock()
    print("All Best Time to Buy and Sell Stock unit tests passed successfully!")
