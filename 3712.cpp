class Solution {
public:
    int sumDivisibleByK(vector<int>& nums, int k) {
      unordered_map<int,int> freq;
      int sum = 0;

      for (int i = 0; i < nums.size(); i++) {
        freq[nums[i]] += 1;
    }
      for (auto& [num,count] : freq) {
        if (count % k == 0) {
          sum += num*count;
        }
      }
      return sum;
    }
};
