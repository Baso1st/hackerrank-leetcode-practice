#https://leetcode.com/problems/analyze-user-website-visit-pattern/
#1152. Analyze User Website Visit Pattern

from itertools import combinations

class SiteVisit:
    def __init__(self, site_name, time):
        self.site_name = site_name
        self.time = time

class Solution:
            
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_table = {}
        
        for idx, user in enumerate(username):
            if user in user_table:
                user_table[user].append(SiteVisit(website[idx], timestamp[idx]))
            else:
                user_table[user] = [SiteVisit(website[idx], timestamp[idx])]
        
        
        for key, value in user_table.items():
            user_table[key] = self.get_pattern(value)
        
        pattern_table = {}
        
        for key, patterns in user_table.items():
            for tup in patterns:
                if tup in pattern_table:
                    pattern_table[tup] += 1
                else:
                    pattern_table[tup] = 1
        
        
        freq_pattern = ()
        freq = 0
        
        for key, value in pattern_table.items():
            if value > freq:
                freq_pattern = key
                freq = value
            elif value == freq:
                freq_pattern = min(key, freq_pattern)
        
        return list(freq_pattern)
    
    
    def get_pattern(self, visits):
        combs = list(combinations(visits, 3))
        patterns = set()
        for comb in combs:
            sorted_comb = sorted(comb, key=lambda x: x.time)
            pattern = tuple([x.site_name for x in sorted_comb])      
            patterns.add(pattern)

        return patterns