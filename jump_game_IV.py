class Solution {
public:
    int steps(int i,
              vector<int>& nums,
              unordered_map<int, vector<int>>& mp,
              vector<int>& vis) {
        if (i >= nums.size() - 1) return 0;
        if (vis[i]) return INT_MAX;
        vis[i] = 1;
        int ans = INT_MAX;
        vector<int>& temp = mp[nums[i]];
        int next = steps(i + 1, nums, mp, vis);
        if (next != INT_MAX)
            ans = min(ans, 1 + next);
        if (i >= 1) {
            next = steps(i - 1, nums, mp, vis);
            if (next != INT_MAX)
                ans = min(ans, 1 + next);
        }
        for (int j = 0; j < temp.size(); j++) {
            if (temp[j] != i) {
                next = steps(temp[j], nums, mp, vis);
                if (next != INT_MAX)
                    ans = min(ans, 1 + next);
            }
        }
        vis[i] = 0;
        return ans;
    }

    int minJumps(vector<int>& arr) {
        unordered_map<int, vector<int>> mp;
        for (int i = 0; i < arr.size(); i++)
            mp[arr[i]].push_back(i);
        vector<int> vis(arr.size(), 0);
        return steps(0, arr, mp, vis);
    }
};
