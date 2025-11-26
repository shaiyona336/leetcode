
class Solution {
private:
  bool is_balanced(unordered_map<char,int>& freq) {
    int target = freq.begin()->second;
    for (auto& digit : freq) {
      if (digit.second != target) {
        return false;
      }
    }
    return true;
  }



public:
    int longestBalanced(string s) {
      int best = 0;
      
      for (int i = 0; i < s.size(); i++) {
        unordered_map<char,int> freq;
        for (int j = i; j<s.size(); j++) {
          freq[s[j]] += 1;
          if (j - i + 1 < best) {
            continue;
          }
          if (is_balanced(freq)) {
              best = max(best,j-i+1);
              }
            }
          }



      return best;
        
    }
};

