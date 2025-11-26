impl Solution {
    pub fn count_valid_selections(nums: Vec<i32>) -> i32 {
        let size = nums.len();
        let mut sum = 0;

        for index in 0..size { 
            for direction in 0..=1 { 
                if nums[index] == 0 {
                    if Solution::check_valid_pos(nums.clone(),index,direction) {
                        sum += 1;
                    }
                }
            }
        }

        return sum as i32;
    }

    pub fn check_valid_pos(mut nums: Vec<i32>, index: usize, direction: usize) -> bool { 
        let mut direction = direction;
        let mut index = index;
        let mut index = index as i32;
        loop {
            if index < 0 || index as usize >= nums.len() {
                break;
            }
            if nums[index as usize] == 0 {
                if direction == 1 {
                    index += 1;
                }
                else {
                    index -= 1;
                }
            } else {
                nums[index as usize] -= 1;
                if direction == 1 {
                    direction = 0;
                    index -= 1;
                } else {
                    direction = 1;
                    index += 1;
                }
            }
        }

        for i in 0..nums.len() {
            if nums[i] != 0 {
                return false;
            }
        }

        return true;
    }
}
