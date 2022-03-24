from typing import List
class Solution:
    # greedy solution: heaviest people need to be on a boat, if lightest person not yet on boat can 
    # fit, put them on, otherwise heaviest has to be alone
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        # j index of heaviest person not yet on a boat
        j = len(people) - 1
        
        # enumerate through lightest people on the boat
        for i, lighter in enumerate(people):
            # calculate space left on boat if lightest person gets on
            space_left = limit - lighter
            
            # send all people who are too heavy to fit with lightest person by themselves 
            while j > i and people[j] > space_left:
                j -= 1
            
            # if all people have been sent on boat break
            if j <= i:
                break
            
            # people[j] fits on boat with lightest, so send them as a pair and get next heaviest person
            j -= 1
        
        # amount of boats needed is total amount of people minus light people who paired up with heavy person
        return len(people) - i