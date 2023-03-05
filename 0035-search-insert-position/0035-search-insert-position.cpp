class Solution {
public:
    int searchInsert(vector<int>& arr1, int target) {
        
        return lower_bound(arr1.begin(), arr1.end(), target)
                - arr1.begin();
    }
};