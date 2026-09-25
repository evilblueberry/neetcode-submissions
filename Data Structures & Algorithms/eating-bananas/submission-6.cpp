class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        if (piles.empty()) return false;

        int l = 1, r = *std::max_element(piles.begin(), piles.end());
        int total_bananas = 0;
        int minimum_k = r;
        for (int i = 0; i < piles.size(); i++) {
            total_bananas += piles[i];
        }

        while (l <= r) {
            int hours = 0;
            int m = (l + r) / 2;

            for (int pile : piles) {
                hours += (pile + m - 1) / m;
            }

            std::cout << "hours: " << hours << std::endl;
            std::cout << "l: " << l << std::endl;
            std::cout << "r: " << r << std::endl;

            if (hours <= h) {
                if (m < minimum_k) {
                    minimum_k = m;
                    
                }
                r = m - 1;
            } else {

                l = m + 1;
            }
        }

        return minimum_k;
    }
};
