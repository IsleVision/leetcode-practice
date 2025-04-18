class Solution {
    public String countAndSay(int n) {
        if(n==1){
            return "1";
        }

        String temp = countAndSay(n-1);
        int length = temp.length();
        StringBuilder result = new StringBuilder("1"+temp.charAt(0));
        for(int i=1; i<length; i++){
            if(result.charAt(result.length()-1)!=temp.charAt(i)){
                result.append("1"+temp.charAt(i));
            }
            else{
                int cnt = result.charAt(result.length()-2)-'0';
                result.setCharAt(result.length()-2,((cnt+1)+"").charAt(0));
            }
        }
        System.out.println(n+" "+temp+" "+result);
        return result.toString();
    }
}