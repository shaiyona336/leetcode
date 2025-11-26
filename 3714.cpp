class Solution {
public:
    int longestBalanced(string s) {
      int output = 0;
      int size = s.size();
      //case 1
      int i = 0;
      while (i < size) {
        int j = i;
        while (j < size and s[j] == s[i]) {
          j++;
        }
        output = max(output,j-i);
        i = j;
      }
      //case 2
      vector<pair<char,char>> pairs = {{'a','b'},{'a','c'},{'b','c'}};
      for (auto [char1, char2] : pairs) {
        unordered_map<int,int> last_seen;
        last_seen[0] = -1;
        int diff = 0;
        for (int i = 0; i < size; i++) {
          if (s[i] == char1) {
            diff += 1;
          } else if (s[i] == char2) {
            diff -= 1;
          } else {
            last_seen.clear();
            last_seen[0] = i;
            diff = 0;
          }
          if (last_seen.count(diff) == 0) {
            last_seen[diff] = i;
          } else {
            output = max(output, i-last_seen[diff]);
          }
        }
      }
      //case 3
      map<pair<int,int>,int> triples;
      triples[{0,0}] = -1;
      int count_a = 0;
      int count_b = 0;
      int count_c = 0;
      int diff_ba = 0;
      int diff_ca = 0;
      for (int i = 0; i < size; i += 1) {
        if (s[i] == 'a') {
            count_a++;
        } else if (s[i] == 'b') {
            count_b++;
        } else {
            count_c++;
        }
        diff_ba = count_b - count_a;
        diff_ca = count_c - count_a;
        pair<int,int> diff = {diff_ba,diff_ca};
        if (triples.count(diff) == 0) {
            triples[diff] = i;
        } else {
            output = max(output,i-triples[diff]);
        }
      }

      return output;        
    }
};

