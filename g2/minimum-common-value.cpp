class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
      int value1 = nums2[0];
      int length;

      length = nums1.size();
      int length2 = nums2.size();

      int returned = length;
      
      int index = 0;
      
      int right = 0;

      while (index < returned){  
          while (right < nums2.size() && nums2[right] < nums1[index]){
              right++;
          }
          if (right < nums2.size()){
          if (nums1[index] == nums2[right]) return nums2[right];
          }
          index++;
      }
    //   if (index < returned && nums1[index] == nums2[0]){
    //       return nums2[0];
    //   }
      return -1;
    }
};