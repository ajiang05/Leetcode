class Solution {
    public boolean checkIfPangram(String sentence) {
        HashSet<Character> unique = new HashSet<>();
        for(int i =0;i<sentence.length();i++){
            unique.add(sentence.charAt(i));
            if (unique.size()==26){
                return true;
            }
        }
        return false;
    }
}