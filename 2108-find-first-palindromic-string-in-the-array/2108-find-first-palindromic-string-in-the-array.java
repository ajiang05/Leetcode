class Solution {
    public String firstPalindrome(String[] words) {
        //Go through each word and check two pointer
        for(String word:words){
            int l = 0;
            int r = word.length()-1;

            boolean isPalindrome = true;
            while(l<=r){
                if(word.charAt(l)!=word.charAt(r)){
                    isPalindrome = false;
                    break;
                }
                l+=1;
                r-=1;
            }

            if(isPalindrome){
                return word;
            }
        }

        return "";
    }
}