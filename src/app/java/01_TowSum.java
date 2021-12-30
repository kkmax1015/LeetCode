package app.java;

import java.util.HashMap;
import java.util.Map;

class Solution1 {

    public static void main(String[] args) throws Exception {
        int[] inputNums = new int[] { 2, 7, 11, 15 };
        int inputTarget = 9;
        int[] ans = twoSum(inputNums, inputTarget);
        System.out.println(ans[0] + "," + ans[1]);
    }

    //　自分の解答
    public static int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            int subTarget = target - nums[i];
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] == subTarget) {
                    return new int[] { i, j };
                }
            }
        }
        throw new IllegalArgumentException("targetとなる組み合わせが見つかりません");
    }
    
    // 模範解答
    public int[] twoSum_answer(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}