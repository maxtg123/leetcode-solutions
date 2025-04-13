class Solution {
    public int reverse(int x) {
        int temp, rem, flag=0;
        long res=0;
        temp = x;
        if(x<0){
            x=x*-1;
            flag=1;
        }
        while(x>0){
            rem = x % 10;
            res = (res * 10) + rem;
            x = x / 10;
        }
        if(flag==1){
            res=res*-1;
        }
        if(res < Math.pow(-2,31) || res > (Math.pow(2,31) -1))
        {
            return 0;
        }
        else{
            return (int) res;
        }
    }
  }
