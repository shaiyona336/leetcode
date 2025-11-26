impl Solution {
    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {
        let mut possibilities: Vec<Vec<Vec<char>>> = Vec::new();
        //initialize possibilities for every cell
        for y in 0..=9 {
            let mut row = Vec:new();
            for x in 0..=9 {
                let possible: Vec<char>;
                if board[y][x] != '.':
                    possible = ('1'..='9').collect();
                else {
                    possible = board[y][x];
                }
                row.push(possible);
            }
            possibilities.push(row);
        }
    }

    pub fn remove_impossible(possibilities: Vec<Vec<Vec<char>>>) {


    }

    pub fn remove_box(possibilities: Vec<Vec<Vec<char>>>, u32 row, u32 col, char digit) {
        for y in range row*3..row*3+3 {
            for x in range col*3..col*3+3 {
                
            }
        }
        
    }
    pub fn remove_right_line(possibilities: Vec<Vec<Vec<char>>>, u32 row, char digit) {
        
    }
    pub fn remove_top_line(possibilities: Vec<Vec<Vec<char>>>, u32 col, char digit) {
        
    }
}
