

class Solution {
    public int firstUniqChar(String s) {
        //We get the frequency of letters in stirn gs then go back and check whcih one have freq 1

        int[] arr = new int[26];
        for(int i = 0; i<s.length();i++){
            arr[s.charAt(i) - 'a']++;
        }
        for(int i = 0;i<s.length();i++){
            if(arr[s.charAt(i)-'a']==1){
                return i;
            }
        }
        return -1;
    }
}