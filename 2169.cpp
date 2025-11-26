class Solution {
public:
    int countOperations(int num1, int num2) {
      int count = 0;

      while (num1 != 0 and num2 != 0) {
        count += 1;
        if (num2 > num1) {
          num2 -= num1;
        } else {
          num1 -= num2;
        }
      }

      return count;
    }
};
