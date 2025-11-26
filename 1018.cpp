class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
      std::vector<bool> output;
      long long curr_num = 0;

      for (int i = 0; i < nums.size(); i++) {
        curr_num = (curr_num << 1) % 10;
        curr_num += nums[i];
        if (curr_num % 5 == 0) {
          output.push_back(true);
        } else {
          output.push_back(false);
        }
      }

      return output;
    }
};
