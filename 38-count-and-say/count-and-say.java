class Solution {
    public String countAndSay(int n) {
        if(n==1){
            return "1";
        }

        String temp = countAndSay(n-1);
        int length = temp.length();
        String result = "1"+temp.charAt(0);
        for(int i=1; i<length; i++){
            if(result.charAt(result.length()-1)!=temp.charAt(i)){
                result +="1"+temp.charAt(i);
            }
            else{
                int cnt = result.charAt(result.length()-2)-'0';
                result = result.substring(0,result.length()-2)+(cnt+1)+result.substring(result.length()-1);
            }
        }
        return result;
    }
}