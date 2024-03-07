class Pair{

    int a;
    int b;

    Pair(int a , int b){
        this.a = a;
        this.b = b;
    }
}

class Solution {

    public void mergeSort(int[][] intervals , int i , int j , int high){

        int[][] t = new int[intervals.length][2];
        int k = i;
        int x = j;
        j++;
        int temp = i;

        while(i <= x && j <= high){

            if(intervals[i][0] < intervals[j][0]){

                t[k][0] = intervals[i][0];
                t[k][1] = intervals[i][1];
                k++;
                i++;
            }
            else{
                
                t[k][0] = intervals[j][0];
                t[k][1] = intervals[j][1];
                k++;
                j++;
            }
        }

        while(i <= x){

            t[k][0] = intervals[i][0];
            t[k][1] = intervals[i][1];
            k++;
            i++;
        }

        while(j <= high){

            t[k][0] = intervals[j][0];
            t[k][1] = intervals[j][1];
            k++;
            j++;
        }

        for(i = temp ; i <= high ; i++){

            intervals[i][0] = t[i][0];
            intervals[i][1] = t[i][1];
        }
    }


    public void divide(int[][] intervals , int low , int high){

        if(low >= high) return;

        int mid = (low+high)/2;
        divide(intervals , low , mid);
        divide(intervals , mid+1 , high);
        mergeSort(intervals , low , mid , high);
    }

    public int[][] merge(int[][] intervals) {
        
    divide(intervals , 0 , intervals.length-1);

    // for(int i=0 ; i<intervals.length ; i++)
    //     System.out.println(Arrays.toString(intervals[i]));

    LinkedList<Pair> t = new LinkedList<>();
    t.add(new Pair(intervals[0][0] , intervals[0][1]));
    
    // System.out.println(intervals[1][0]+ " H I " + t.get(t.size()-1).b);

       for(int i=1 ; i< intervals.length ; i++){

        //    for(int ss = 0 ; ss<t.size() ; ss++)
        //         System.out.print(t.get(ss).a + " " + t.get(ss).b + " ");
        //     System.out.println();

           int n = t.size();

           if(intervals[i][0] <= (t.get(n-1)).b){

               Pair s = t.remove(n-1);
            //    System.out.println(s.a + " " + s.b);
               int x = (intervals[i][1] > s.b) ? intervals[i][1] : s.b;
               int y = (intervals[i][0] < s.a) ? intervals[i][0] : s.a;
               
               t.add(new Pair(y , x)); 
           }
           else{

               t.add(new Pair(intervals[i][0] , intervals[i][1]));
           }
           
       }

        int[][] res = new int[t.size()][2];
        for(int i=0 ; i<t.size() ; i++){

            res[i][0] = t.get(i).a;
            res[i][1] = t.get(i).b;
        }

        return res;

    }
}