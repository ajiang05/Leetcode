class Solution {
    public int countDigits(int num) {
        int result = 0;
        String num_str = String.valueOf(num);
        for(int i =0; i<num_str.length();i++){
            int digit = num_str.charAt(i)-'0';
            if(num%digit==0){
                result+=1;
            }
        }
        return result;
    }
}