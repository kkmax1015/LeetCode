package app;

class Solution1 {

    public static void main(String[] args) throws Exception {
        int[] inputNums = new int[] { 2, 7, 11, 15 };
        int inputTarget = 9;
        int[] ans = twoSum(inputNums, inputTarget);
        System.out.println(ans[0] + "," + ans[1]);
    }

    public static int[] twoSum(int[] nums, int target) {
        for(int i=0; i < nums.length;i++){
            int subTarget = target - nums[i];
            for(int j=i+1; j < nums.length;j++){
                if(nums[j]==subTarget){
                    return new int[] {i,j};
                }
            }
        }
        throw new IllegalArgumentException("targetとなる組み合わせが見つかりません");
    }
}