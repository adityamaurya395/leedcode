class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        vector<int> v;

        merge(nums1.begin(), nums1.end(),
              nums2.begin(), nums2.end(),
              back_inserter(v));

        int n = v.size();

        if (n % 2 == 1)
            return v[n / 2];

        return (v[n / 2] + v[n / 2 - 1]) / 2.0;
    }
};