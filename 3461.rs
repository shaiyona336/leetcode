impl Solution {
    pub fn has_same_digits(s: String) -> bool {
        let mut s = s;
        
        while s.len() > 2 {
            let chars: Vec<char> = s.chars().collect();
            let mut next = String::new();

            for i in 0..chars.len()-1 {
                let first = chars[i].to_digit(10).unwrap();
                let second = chars[i+1].to_digit(10).unwrap();
                let next_char = ((first+second)%10) as u32;
                next.push(std::char::from_digit(next_char,10).unwrap());
            }
            s = next;

        }
        if s.chars().nth(0).unwrap() == s.chars().nth(1).unwrap() {
            return true;
        }
        false
    }
}
