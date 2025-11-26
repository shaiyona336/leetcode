class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (const string& str : strs) {
          int zeroes = 0;
          int ones = 0;
          for (char c : str) {
            if (c == '0') {
              zeroes++;
            } else {
              ones++;
            }
          }
        

          for (int x = m; zeroes >= x; x--) {
            for (int y = n; y >= ones; y--) {
              dp[x][y] = max(dp[x][y], dp[x-zeroes][y-ones]+1);
            }
          }
        }

        return dp[m][n];
    }
};
