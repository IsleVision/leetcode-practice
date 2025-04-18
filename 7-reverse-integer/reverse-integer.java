class Solution {
    public int reverse(int x) {
        String num = x + "", numDigs;
        StringBuilder rev = new StringBuilder("");
        if(num.charAt(0)=='-'){
            numDigs = num.substring(1);
            rev = rev.append("-");
        }
        else{
            numDigs = num;
        }

        int length = numDigs.length();
        for(int i=0; i<length; i++){
            rev.append(numDigs.charAt(length-1-i)+"");
        }

        int res;
        try{
            res = Integer.parseInt(rev.toString());
        }
        catch(Exception e){
            res=0;
        }

        return res;

    }
}