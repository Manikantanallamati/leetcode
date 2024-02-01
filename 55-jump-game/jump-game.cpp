#include <iostream>
#include <vector>

class Solution {
public:
    bool canJump(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> dp(n, -1);
        return Fun(0, nums, n, dp);
    }

    bool Fun(int idx, const std::vector<int>& nums, int n, std::vector<int>& dp) {
        if (idx >= n) {
            return false;
        }
        if (idx == n - 1) {
            return true;
        }
        if (dp[idx] != -1) {
            return dp[idx];
        }
        dp[idx] = 0;
        for (int i = 1; i <= nums[idx]; ++i) {
            if (Fun(idx + i, nums, n, dp)) {
                dp[idx] = 1;
                return dp[idx];
            }
        }
        return dp[idx];
    }
};

// int main() {
//     Solution sol;
//     std::vector<int> nums = {2, 3, 1, 1, 4};
//     bool result = sol.canJump(nums);
//     std::cout << (result ? "true" : "false") << std::endl;

    // return 0;
// }
