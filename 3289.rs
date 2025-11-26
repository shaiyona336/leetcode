use std::collections::HashSet;
impl Solution {
    pub fn get_sneaky_numbers(nums: Vec<i32>) -> Vec<i32> {
        let mut arr: Vec<i32> = Vec::new();
        let mut alreadySeen = HashSet::new();
        let mut index = 0;

        for &num in &nums {
            if alreadySeen.contains(&num) {
                arr.push(num);
            } else {
                alreadySeen.insert(num);
            }
        }
    return arr;
    }
}
