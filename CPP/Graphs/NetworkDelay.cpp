#include <list>
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        //create adjancency list
        vector<list<pair<int, int>>> adj(n + 1, list<pair<int, int>>());
        for(int i=0; i<times.size(); i++){
            int u = times[i][0];
            int v = times[i][1];
            int w = times[i][2];

            adj[u].push_back(make_pair(v,w));
        }

        vector<int> dist(n+1, INT_MAX);
        set<pair<int, int>> st;
        dist[k] = 0;
        st.insert(make_pair(0, k));

        while(!st.empty()){
            //fetch top node
            auto top = *(st.begin());
            int nodeDistance = top.first;
            int topNode = top.second;

            st.erase(st.begin()); //remove top record

            //traverse on neighbors
            for(auto neighbor : adj[topNode]){
                if(nodeDistance + neighbor.second < dist[neighbor.first]){
                    auto record = st.find(make_pair(dist[neighbor.first], neighbor.first));

                    // if record found, erase it
                    if(record != st.end()){
                        st.erase(record);
                    }
                    // update the distance
                    dist[neighbor.first] = nodeDistance + neighbor.second;
                    // insert the record in set
                    st.insert(make_pair(dist[neighbor.first], neighbor.first));
                }
            }
        }

        int mn = 0;
            for (int i = 1; i <= n; i++)
            {
                mn = max(mn, dist[i]);
            }
        return mn == INT_MAX ? -1 : mn;

    }
};