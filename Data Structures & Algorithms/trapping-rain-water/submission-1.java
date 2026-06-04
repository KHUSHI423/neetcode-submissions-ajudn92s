class Solution {
    public int trap(int[] height) {
        int leftmax=0;
        int rightmax =0;
        int water =0;
        int l =0 ;
        int r = height.length-1;
        while(l<r){
            if(height[l]<height[r]){
                if(height[l]>leftmax) leftmax= height[l];
                else{
                        water+=(leftmax -height[l]);
                        l+=1;
                }

            }
            else{
                if(height[r]>rightmax) rightmax= height[r];
                else{
                        water+=(rightmax -height[r]);
                        r-=1;
                }
            }
        }
        return water;
        
    }
}
