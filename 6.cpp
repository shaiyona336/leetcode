class Solution {
public:
  int find_row(int index, int numRows) {
    int output;
    index %= ((numsRows-1)*2);
    if (index < numRows) {
      output = numRows-index;
    } else {
      index %= numRows;
      output = index;
    }
    
    return output;
  }

  int find_new_pos(string s, int index, int numRows, bool going_down) {
    int curr_row = find_row(index,numRows);
    int how_many_to_add;
    
    if (going_down) {
      how_many_to_add = index*2;
    } else {
      how_many_to_add = ((numRows-1)-currRow)*2;
    }

    return index+how_many_to_add;
  }

    string convert(string s, int numRows) {
        
    }
};





//need to build the string in zigzag
//need to take from currect place in original string the next char
//need to find for every index from 0 to len(string) f(char_new_pos) where
//f(char_new_pos) = char_old_pos
//f(char_new_pos) = *
//P(0)        I(6)         N(12)
//A(1)   L(5) S(7)   I(11) G(13)
//Y(2) A(4)   H(8) R(10)
//P(3)        I(9)
//0=0
//1=6
//2=12
//3=1
//4=5
//5=7
//6=11
//7=13
//8=2
//9=4
//10=8
//11=10
//12=3
//13=9
//
//
//height goes from nums_rows->0->num_rows
//%(num_rows*2)
//if index>num_rows -> else
