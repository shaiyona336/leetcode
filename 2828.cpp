class Solution {
private:
  bool is_possible(vector<int>& stations, int r, int k, long long target) {
    long long curr_k = k;
    int index = 0;
    int size = stations.size();
    vector<long long> power_pos(stations.size());
    vector<long long> diff(stations.size()+1,0);
    long long curr_diff = 0;
    long long add_electric;
    long long sliding_window_sum = 0;

    for (int i = 0; i <= min((int)stations.size()-1,r); i++) {
      sliding_window_sum += stations[i];
    }

    power_pos[0] = sliding_window_sum;

    for (int i = 1; i < stations.size(); i++) {
      int left = i-r-1;
      int right = i+r;
      if (left >= 0) {
        sliding_window_sum -= stations[left];
      }
      if (right < stations.size()) {
        sliding_window_sum += stations[right];
      }
      power_pos[i] = sliding_window_sum;
    }






    while (index < size) {
      curr_diff += diff[index];
      power_pos[index] += curr_diff;
      if (curr_k < 0) {
        return false;
      }
      if (power_pos[index] < target) {
        add_electric = target - power_pos[index];
        if (curr_k < add_electric) {
            return false;
        }
        curr_k -= add_electric;
        int pos_new_electric = min((int)stations.size()-1,index+r);
        diff[max(0,pos_new_electric-r)] += add_electric;
        diff[min((int)stations.size(),pos_new_electric+r+1)] -= add_electric;
        curr_diff += add_electric;

      }
      index += 1;
      
    }
    return true;

  }



public:
    long long maxPower(vector<int>& stations, int r, int k) {
      long long result = 0;
      long long min_electric = 0;
      long long max_electric = 0;
      long long mid_electric;


      for (int power_city : stations) {
        max_electric += power_city;
      }
      max_electric += k;


      while (min_electric <= max_electric) {
        mid_electric = min_electric + (max_electric-min_electric) / 2;
        if (is_possible(stations,r,k,mid_electric)) {
          result = mid_electric;
          min_electric = mid_electric+1;
        } else {
          max_electric = mid_electric-1;
        }
      }

      return result;
        
    }
};
