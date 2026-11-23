class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        auto seen = unordered_map<int, int>{};
        for (int i = 0; i < static_cast<int>(size(nums)); i++) {
            int rem = target - nums[i];

            if (seen.contains(rem)) {
                return vector{seen[rem], i};
            }
            seen[nums[i]] = i;
        }
    }
};
