/**
 * Solution to Find the Duplicate Number at LeetCode in Java
 *
 * author: hellache
 * ref: https://leetcode.com/problems/find-the-duplicate-number/
 */
class Solution {
    public int findDuplicate(int[] nums) {
        int p1=nums[0];
        int p2=nums[0];
        p1=nums[p1];
        p2=nums[nums[p2]];
        while(p1!=p2){
            p1=nums[p1];
            p2=nums[nums[p2]];
        }
        p1=nums[0];
        while(p1!=p2){
            p1=nums[p1];
            p2=nums[p2];
        }
        return p1;
    }
}
