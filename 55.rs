impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let size = nums.len();
        if size == 0 {
            return true;
        }
        let mut fuel = nums[0];
        let mut curr_index = 0;
        
        while curr_index < size {
            if fuel == 0 {
                return false;
            }
            curr_index += 1;
            fuel -= 1;
            fuel = fuel.max(nums[curr_index]);
        }

        return true;
    }
}
