class Solution {
private:
  vector<int> parent;
  vector<bool> is_connected;
  unordered_map<int, priority_queue<int, vector<int> ,greater<int>>> tree;

  int find(int x) {
    if (parent[x] != x) {
      parent[x] = find(parent[x]);
    }
    return parent[x];
  }

  void unite(int x, int y) {
    int parent_x,parent_y;
    parent_x = find(x);
    parent_y = find(y);
    parent[parent_y] = parent_x;
    
  }

public:
    vector<int> processQueries(int c, vector<vector<int>>& connections, vector<vector<int>>& queries) {
      vector<int> result;
      parent.resize(c+1);
      is_connected.resize(c+1);

      for (int i = 1; i <= c; i++) {
        parent[i] = i;
        is_connected[i] = true;
      }

      for (auto& arc : connections) {
        unite(arc[0],arc[1]);
      }

      for (int i = 1; i <= c; i++) {
        tree[find(i)].push(i);
      }
      
      for (auto& query : queries) {
        int type = query[0];
        int value = query[1];
        
        if (type == 1) {
          if (is_connected[value]) {
            result.push_back(value);
          } else {
            priority_queue<int, vector<int> ,greater<int>>& curr_tree = tree[find(value)];
            while (!curr_tree.empty() && !is_connected[curr_tree.top()]) {
              curr_tree.pop();
            }
            if (curr_tree.empty()) {
              result.push_back(-1);
            } else {
              result.push_back(curr_tree.top());
            }
        }
        } else {
          is_connected[value] = false;
        }
      }
      return result;

    }
};
