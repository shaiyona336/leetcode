impl Solution {
    pub fn number_of_beams(bank: Vec<String>) -> i32 {
        let mut lasers_before = 0;
        let mut curr_row_index = 0;
        let size_rows = bank.len();
        let size_columns = bank[0].len();
        let mut sum_lasers = 0;

        while curr_row_index < size_rows {
            let mut curr_column_index: usize = 0;
            let mut curr_row_lasers = 0;
            while curr_column_index < size_columns {
                if let Some(ch) = bank[curr_row_index].chars().nth(curr_column_index) {
                    if ch == '1' {
                    curr_row_lasers += 1;
                }
            }
                curr_column_index += 1;
            }
            if curr_row_lasers == 0 && lasers_before == 0 {
                lasers_before = curr_row_lasers;
            }
            else if curr_row_lasers != 0 {
                sum_lasers += curr_row_lasers * lasers_before;
                lasers_before = curr_row_lasers;
            }
            curr_row_index += 1;
        }

        return sum_lasers;
    }
}
