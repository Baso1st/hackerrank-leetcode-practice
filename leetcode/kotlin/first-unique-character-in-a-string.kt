//https://leetcode.com/problems/first-unique-character-in-a-string/submissions/
//387. First Unique Character in a String

import kotlin.math.*
import kotlin.collections.HashMap
// T: O(N)
// S: O(1)
class Solution {
    fun firstUniqChar(s: String): Int {
        var map = HashMap<Char, Int>()
        for (c in s){
            map[c] = map.getOrDefault(c, 0) + 1
        }

        for ((idx, c) in s.withIndex()){
            if(map[c] == 1){
                return  idx
            }
        }
        return  -1
    }
}