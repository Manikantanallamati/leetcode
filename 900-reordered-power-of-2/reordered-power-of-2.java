class Solution {

    // boolean ans = false;
    public boolean help(int ind , ArrayList<Integer> a , int[] v , int temp){

        if(ind == a.size()) {

            // System.out.println(temp + " " + ans);
            if((temp & (temp-1)) == 0) return true;
            return false;
        }

        // if(ans) return;
        boolean ans = false;

        for(int i=0 ; i<a.size() ; i++){

            if(v[i] == 0){

                if(temp == 0 && a.get(i) == 0) continue;

                v[i] = 1;
                // temp = temp*10 + a.get(i);
                ans |= help(ind+1 , a , v , (temp*10 + a.get(i)));
                v[i] = 0;
            }
        }

        return ans;
    }

    public boolean reorderedPowerOf2(int n) {
        
        ArrayList<Integer> a = new ArrayList<>();
        while(n > 0){

            a.add(n%10);
            n /= 10;
        }

        int[] v = new int[a.size()];

        return help(0 , a , v , 0);
    }
}