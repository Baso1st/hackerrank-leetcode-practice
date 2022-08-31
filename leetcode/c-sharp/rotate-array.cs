// https://leetcode.com/problems/rotate-array/
// 189. Rotate Array


public class Solution {
    public void Rotate(int[] nums, int k) {
        var n = nums.Length;
        k = k % n;
        Reverse(0, n-k-1, nums);
        Reverse(n-k, n-1, nums);
        Reverse(0, n-1, nums);
    }
    
    public void Reverse(int start, int end, int[] nums){
        while (start < end) {
            (nums[start], nums[end]) = (nums[end], nums[start]);
            start++;
            end--;
        }
    }
}