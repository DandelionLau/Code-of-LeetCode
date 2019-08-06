class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int len = nums.size();
        int result = 0;
        int temp = 0;
        int diff = 0;
        int min_diff = 1000;
        for(int i=0;i<len;i++){
            for(int j=i+1;j<len;j++){
                for(int k=j+1;k<len;k++){
                    temp = nums[i]+nums[j]+nums[k];
                    diff = abs(target-temp);
                    if (diff<=min_diff){
                        min_diff = diff;
                        result = temp;
                    }

                }
            }
        }
        return result;
    }
};
