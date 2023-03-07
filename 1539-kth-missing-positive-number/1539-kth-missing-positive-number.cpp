class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {

      int i = 1;
      int maximum = arr[arr.size() - 1];
      
      int index = 0;
      int saved = k;
      for (; i <= maximum + saved; i++){

          if (i != arr[index]){
              k--;
              if (k == 0){
                  
                  saved = i;
                  break;
              }
          }
          else{
              if (index < arr.size() - 1) index++;
          }
      }
    return saved;
    }
};