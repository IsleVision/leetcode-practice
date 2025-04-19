class Solution {
    public int longestConsecutive(int[] nums) {
        int length = nums.length;
        if(length==0){
            return 0;
        }

        Arrays.sort(nums);
        int pre = nums[0];
        int maxL=1,curL=1;
        for(int i=1; i<length; i++){
            if(nums[i]==pre+1){
                curL++;
                if(curL>maxL){
                    maxL=curL;
                }
            }
            else if(nums[i]!=pre){
                curL=1;
            }
            pre=nums[i];
        }

        return maxL;








        // List<List<Integer>> agg = new LinkedList<>();
        // agg.add(new LinkedList(Arrays.asList(nums[0])));
        // for(int i=1; i<length; i++){
        //     boolean added = false;
        //     int cur = nums[i];
        //     for(List<Integer> subAgg: agg){
        //         if(cur==subAgg.get(0)-1){
        //             subAgg.add(0,cur);
        //             added = true;
        //         }
        //         else if(cur==subAgg.get(subAgg.size()-1)+1){
        //             subAgg.add(cur);
        //             added = false;
        //         }
        //     }
        //     if(!added){
        //         agg.add(new LinkedList<>(Arrays.asList(cur)));
        //     }
        // }

        // int maxLength=0;
        // for(List<Integer> subAgg: agg){
        //     if(subAgg.size()>maxLength){
        //         maxLength = subAgg.size();
        //     }
        // }

        // return maxLength;
    
    }
}