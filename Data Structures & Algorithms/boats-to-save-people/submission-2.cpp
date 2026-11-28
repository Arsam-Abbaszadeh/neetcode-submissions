class Solution {
public:
    int numRescueBoats(std::vector<int>& people, int limit) {
        int vecLen = *std::max_element(people.begin(), people.end()) + 1;
        std::vector countSortedWeight(vecLen, 0);
        for (auto weight: people) {
            countSortedWeight[weight]++;
        }

        size_t l {1}, r {countSortedWeight.size() - 1};
        int count{0};
        while (l <= r) {
            while (l <= r &&countSortedWeight[l] <= 0) l++;
            while (l <= r &&countSortedWeight[r] <= 0) r--;
            if (l > r) break;

            if (l + r <= limit) {
                countSortedWeight[l]--;
            }
            countSortedWeight[r]--;
            count++;
        }

        return count;
    }
};