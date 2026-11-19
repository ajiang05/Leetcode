class Solution {
    public int differenceOfSum(int[] nums) {
        int digit_sum = 0;
        int element_sum = 0;

        for(int num: nums){
            element_sum+=num;
            while(num>0){
                int digit = num%10;
                digit_sum+=digit;
                num/=10;
            }
        }

        return element_sum-digit_sum;

    }
}