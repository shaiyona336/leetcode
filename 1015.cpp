class Solution {
public:
    int smallestRepunitDivByK(int k) {
      set<int> alreadySeen;
      int length = 1;
      int left = k - 1;

      while (left != 0) {
        if (alreadySeen.count(left)) {
          return -1;
        }
        alreadySeen.insert(left);
        length++;
        left = (((left*(10 % k)) - 1 + k) % k);
      }

      return length;
    }
};




//k = 3, n = 1, left = 2
//k = 3, n = 11, left = 1
//given length x,k, f(x,k)=left
//need to find first x so f(x,k) = 0
//what does that mean that f(n,k)=left?
//((n*10+1)*10+1)...X (n_times) % k = left
//f(n+1,k)=(((n*10+1)*10+1)...X (n_time) * 10 )  + 1 % k =
//f(n+1,k) = ((((n*10+1)*10+1)...X (n_time) * 10 ) % k - 1 + k) % k =
//f(n+1,k) = ((left*10) % k - 1 + k) % k =
//f(n+1,k) = ((left*(10 % k)) - 1 + k) % k) =
