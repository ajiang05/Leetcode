class Solution {
    public int mostWordsFound(String[] sentences) {
        int result = 0;
        for(String s: sentences){
            result = Math.max(s.split(" ").length,result);
        }
        return result;
    }
}