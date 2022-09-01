// https://leetcode.com/problems/intersection-of-two-arrays-ii/
// 350. Intersection of Two Arrays II 

import kotlin.math.min

class Solution {
    fun intersect(nums1: IntArray, nums2: IntArray): IntArray {
        val map= HashMap<Int, Int>()
        for(num in nums1){
            map[num] = map.getOrDefault(num, 0) + 1
        }

        var result = mutableListOf<Int>()
        for(num in nums2){
            val count = map.getOrDefault(num, 0)
            if (count > 0){
                result.add(num)
                map[num] = count - 1
            }
        }
        return result.toIntArray()
    }
}