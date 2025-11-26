class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
      int index = 0;
      int size = bits.size();

      while (index < size - 1) {
        if (bits[index] == 1) {
          index++;
        }
        index++;
      }

      if (index == size-1) {
        return true;
      }
      return false;
    }
};
