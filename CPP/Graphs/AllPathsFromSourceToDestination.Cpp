class Solution {


private: 
    void dfs(int node,vector<int> &ans,vector<vector<int>> &res,vector<vector<int>>& graph)
    {
        for(auto neighbor : graph[node]){
                ans.push_back(neighbor);
                dfs(neighbor, ans, res, graph);
                if(neighbor == graph.size() - 1)
                {
                    res.push_back(ans);
                }
                ans.pop_back();
        }
    }
public: 
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<int> ans;
        ans.push_back(0);
        vector<vector<int>> res;
        dfs(0,ans,res, graph);
        return res; 
        //adjList is optional
        // unordered_map<int,list<int>> adj;
        // unordered_map<int,bool> visited;

        // for(int i=0; i<graph.size(); i++){
        //     for(int j=0; j<graph[i].size(); j++){
        //         adj[i].push_back(graph[i][j]);
        //     }
        // }
    }
};