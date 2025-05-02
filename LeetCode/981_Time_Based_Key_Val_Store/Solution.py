class Solution:

    def __init__(self):
        self.tm = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tm:
            self.tm[key][timestamp] = value
        else:
            self.tm[key] = {timestamp:value}

    def get(self, key: str, timestamp: int) -> str:
        value = ""
        if key not in self.tm:
            return ""
        for time in reversed(self.tm[key].keys()):
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