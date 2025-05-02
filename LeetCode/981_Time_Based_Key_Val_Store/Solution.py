import bisect
class Solution:

    def __init__(self):
        self.tm = dict()
        self.prev_times_mp = dict() # finds existing keys

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tm:
            self.tm[key][timestamp] = value
            bisect.insort(self.prev_times_mp[key], timestamp)
        else:
            self.tm[key] = {timestamp:value}
            self.prev_times_mp[key] = [timestamp]
        

    def get(self, key: str, timestamp: int) -> str:
        value = ""
        if key not in self.tm:
            return ""
        for i in range(len(self.prev_times_mp[key])-1,-1,-1):
            time = self.prev_times_mp[key][i]
            if time <= timestamp:
                value = self.tm[key][time]
                break
        return value
    
"""
Approach: Brute Force

Time:
- set: O(n)
- get: O(n)

Space: O(m*n) where m is the number of keys and n is the number of unique timestamps
"""