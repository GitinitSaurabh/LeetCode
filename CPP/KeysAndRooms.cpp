    using namespace std;
class Solution {


public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        vector<bool> visited(rooms.size(), false);
        dfs(0, rooms, visited);
        for(int i=0; i<visited.size(); i++){
            if(!visited[i]){
                return false;
            }
        }
        return true;
    }
public:
    void dfs(int node, vector<vector<int>>& rooms, vector<bool>& visited){

        visited[node] = true;
        for(auto neighbor : rooms[node]){ 
            if(!visited[neighbor]){
                dfs(neighbor, rooms, visited);
            }
        }
    }
};