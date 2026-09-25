class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.empty()) return -1;

        int l = 0, r = nums.size() - 1;

        while (l <= r) {
            int m = (r + l) / 2;
            std::cout << m << std::endl;
            if (nums[m] == target) {
                return m;
            } else if (nums[m] < target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return -1;

    }
};
