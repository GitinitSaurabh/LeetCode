class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        heavy = len(people) - 1
        light = 0
        boats = 0

        while(heavy >= light):
            if(people[heavy] + people[light] <= limit):
                boats += 1
                heavy -= 1
                light += 1
            else : 
                boats += 1
                heavy -=1
        
        return boats

        