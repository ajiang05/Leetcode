class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        //loop through hours and see how many are greater than or equal to target
        int result = 0;
        for(int h: hours){
            if(h>=target){
                result+=1;
            }
        }
        return result;
        
    }
}