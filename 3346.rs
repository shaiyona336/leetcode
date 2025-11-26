use std::collections::{HashMap,HashSet};
impl Solution {
    pub fn max_frequency(nums: Vec<i32>, k: i32, num_operations: i32) -> i32 {
        let mut nums = nums;
        nums.sort_unstable();
        let mut max_freq = 0;
        let mut potential_target = std::collections::HashSet::new();
        let mut amount_num = std::collections::HashMap::new();
        for &num in &nums {
            *amount_num.entry(num).or_insert(0) += 1;
        }
        
        for &num in &nums {
            potential_target.insert(num-k);
            potential_target.insert(num);
            potential_target.insert(num+k);
        }

        for &target in &potential_target {
            let already_good = *amount_num.get(&target).unwrap_or(&0);

            let l = nums.partition_point(|&x| x < target - k);
            let r = nums.partition_point(|&x| x <= target + k);

            let can_reach = r-l;

            let can_actually_get_to = can_reach.min(already_good + num_operations as usize);
            max_freq = max_freq.max(can_actually_get_to);
        }
        max_freq as i32
    }
}
