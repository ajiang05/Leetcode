class Solution {
    public int[] numberGame(int[] nums) {
        //We create an array to store
        //We sort the array then input big then small
        int[] arr = new int[nums.length];
        Arrays.sort(nums);

        for(int i = 0;i<nums.length;i+=2){
            arr[i] = nums[i+1];
            arr[i+1] = nums[i];
        }

        return arr;

    }
}