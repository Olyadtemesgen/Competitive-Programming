class Solution {
public:
    int searchInsert(vector<int>& arr1, int target) {
        //This is my first code that beat 100% 
        return lower_bound(arr1.begin(), arr1.end(), target)
                - arr1.begin();
    }
};