import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Map;

import sun.security.util.Length;

/*
 * @lc app=leetcode.cn id=1 lang=java
 *
 * [1] 两数之和
 */

// @lc code=start
class Solution {
    private static int First; 
    private static ArrayList array;
    private static Object[] ary;
    private static int[] Array;
    private static int Sum;
    public int[] twoSum(int[] nums, int target) {
        array=new ArrayList<>();
        First=0;
        Sum=0;
        for(int i=0;i<nums.length;i++){
            First=nums[i];
            for(int j=0;j<nums.length;j++){
                Sum=First+nums[j];
                if(Sum==target){
                    array.add(i, j);
                }
            }
        }
        ary=array.toArray();
        for(int i=0;i<Array.length;i++){
            Array[i]=(int)ary[i];
        }
        return Array;
    }
}
// @lc code=end

