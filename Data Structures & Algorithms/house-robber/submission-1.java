class Solution {
    int rb( int i, int[] nums,  int[] dp){
        if (i>= nums.length){
            return 0;
        }
        if (dp[i] != -1){
            return dp[i];
        }
        return dp[i] = Math.max( nums[i] + rb(i+2,nums,dp) , rb(i+1,nums,dp));
    }
    public int rob(int[] nums) {
        int n=nums.length;
        int []dp = new int[n];
        Arrays.fill(dp,-1);
        return rb(0,nums,dp);
        
    }
}
