class Solution {
    public boolean isPalindrome(int x) {
        //Convert to stirng then have two poitners
        String num = String.valueOf(x);
        int l = 0;
        int r = num.length()-1;

        while(l<=r){
            if(num.charAt(l++)!=num.charAt(r--)){
                return false;
            }
        }

        return true;
    }
}