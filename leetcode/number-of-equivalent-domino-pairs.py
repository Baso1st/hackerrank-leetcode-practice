#  https://leetcode.com/problems/number-of-equivalent-domino-pairs/

import math


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        #Let's try a bruteforce and see what insights we get from it. 
        
        n = len(dominoes)
        
        for dom in dominoes:
            dom.sort()
            
        #dominoes.sort()

        table = {}
        
       
        
        for dom in dominoes:
            pair = (dom[0], dom[1])
            if pair in table:
                table[pair] += 1
            else:
                table[pair] = 1
        
        count = 0
        for key in table.keys():
            val = table[key]
            if val > 1:
                count += math.comb(val, 2)
    
            
        return count