class Solution {
public:
    int maxOperations(string s) {
      int sum = 0;
      int num_close = 0;
      int num_open = 0;
      int size = s.length();

      for (int i = size-2; i >= 0; i--) {
        if (s[i] == '1') {
          sum += num_open;
          if (s[i+1] == '1') {
            num_close++;
          } else {
            sum += 1;
            num_open++;
          }
      }
      }

      return sum;
    }
};




we need to max operations
last state all the ones in the right
its doesnt matter how many zeroes have between numbers, just if there is or not
can break the problem to get a list of ones and if there is zero or not between them and the next one, and return number of operations
add one after the array ends

the way to maximaize the number of operations is to first move the ones in the left, because they dont change the number of operations to the one after them, and that way they can maximize the amount of operations they themselves doing

i can just run algorithem that while there is a number that can move ->
for each number check if he can move, if so move him to where he can get to from left to right and add operation to the sum

but maybe can calculate to begin with number of operations based on first state

define f(state) = given a state how many operations can make, this is what we need to find

f(index, state) = how many operations the one in index can make given the state
in order to maximize it, he need to move to the next one, and then next one move to the near, and so on
each time someone move, the one last to him if he couldnt move before now hecan
example : (110101) //cooc
(101101) //ococ
(011101) //ccoc
(011011) //cocc
(010111) //occc
(001111); //cccc
(cooc);
(cocc);
(cocc);
(occc);
(cccc);



11110 //ccco
11101 //ccoc
11011 //cocc
10111 //occc
01111 //cccc



1001101 //ococ
0011101 //ccoc
0011011 //cocc
0010111 //occc
0001111 //cccc
    

1000111  //occc


left open -> close
close next open -> switch


every close add opeartions based on opens in the front
every open add 1+numbers of opens in front      

if i go from right to left, i can keep track number of c/o in front
