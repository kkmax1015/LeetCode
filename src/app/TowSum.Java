class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i=0; i < nums.length;i++){
            int subTarget = target - nums[i];
            for(int j=i+1; j < nums.length;j++){
                if(nums[j]==subTarget){
                    return new int[] {i,j};
                }
            }
        }
        throw new IllegalArgumentException("引数の値が不正です");
    }
}