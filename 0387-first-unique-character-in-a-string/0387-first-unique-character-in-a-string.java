

class Solution {
    public int firstUniqChar(String s) {
        //We get the frequency of letters in stirn gs then go back and check whcih one have freq 1

        HashMap<Character,Integer> freq = new HashMap<>();

        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            freq.put(c, freq.getOrDefault(c,0)+1);
        }
        
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(freq.get(c)==1){
                return i;
            }
        }

        return -1;
    }
}