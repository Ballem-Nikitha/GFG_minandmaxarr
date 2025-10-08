class Solution:
    def maxProduct(self, arr):
        max_product = arr[0]
        curr_max = arr[0]
        curr_min = arr[0]

        for i in range(1, len(arr)):
            num = arr[i]

            if num < 0:
                curr_max, curr_min = curr_min, curr_max  # swap when negative number appears

            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            max_product = max(max_product, curr_max)

        return max_product
