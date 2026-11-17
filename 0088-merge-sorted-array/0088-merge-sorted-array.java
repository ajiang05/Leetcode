class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = 0;
        int j = 0;
        
        //Declare array of size 5
        int[] result = new int[5];

        //Declare Array list of 
        ArrayList<Integer> result2 = new ArrayList<>();
    
        while(i<m && j<n){
            if(nums1[i]<=nums2[j]){
                result2.add(nums1[i]);
                i+=1;
            }
            else{
                result2.add(nums2[j]);
                j+=1;
            }
            
        }

        if(i<m){
            for(int num:Arrays.copyOfRange(nums1,i,m)){
                result2.add(num);
            }
        }
        if(j<n){
            for(int num:Arrays.copyOfRange(nums2,j,n)){
                result2.add(num);
            }
        }

        for(int k = 0;k<m+n;k++){
            nums1[k] = result2.get(k);
        }

    }
}