    using namespace std;
class Solution {


public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        vector<bool> visited(rooms.size(), false);
        queue<int> q;
        bfs(0, rooms, visited,q);
        for(int i=0; i<visited.size(); i++){
            if(!visited[i]){
                return false;
            }
        }
        return true;
        
    }
public:
    void bfs(int node, vector<vector<int>>& rooms, vector<bool>& visited, queue<int>& q){

        visited[node] = true;
        q.push(node);
        while(!q.empty()){
            int currNode = q.front();
            q.pop();
            for(auto neighbor : rooms[currNode]){ 
            if(!visited[neighbor]){
                q.push(neighbor);
                visited[neighbor] = true;
                // q.push(neighbor);
                }
            }
        }
        
    }
};