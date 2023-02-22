class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        int mod = 1e9+7;
        long ans = 1;
        vector<long long> dist(n, 1e15), ways(n,0);
        vector<pair<long long,long long>> adj[n]; // u -> v, distance || v -> u, distance

        for(auto it : roads){
            long long u = it[0];
            long long v = it[1];
            long long t = it[2];

            adj[u].push_back({v,t});
            adj[v].push_back({u,t});
        }
        priority_queue< pair<long long,long long>, vector<pair<long long,long long>>, greater<pair<long long, long long>>> pq;
        ways[0] = 1;
        dist[0] = 0;
        pq.push({dist[0],0});
        while(!pq.empty()){
            long long currNode = pq.top().second;
            long long nodeDistance = pq.top().first;
            pq.pop();

            for(auto neighbor : adj[currNode]){
                long long newNodeDistance = (nodeDistance + neighbor.second);
                long long v = neighbor.first;
                    if(newNodeDistance < (dist[v]))
                    {
                        dist[v] = newNodeDistance;
                        pq.push({dist[v],v});
                        ways[v] = ways[currNode];
                        
                    }
                    else if(newNodeDistance == (dist[v])){
                        ways[v] = (ways[v] + ways[currNode])%mod;
                    }
                }
        } 
            
        
        return ways[n-1]%mod;
        
    }
};
