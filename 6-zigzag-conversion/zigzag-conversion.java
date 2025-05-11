class Solution {
    public String convert(String s, int numRows) {
        List<List<String>> al = new LinkedList<>();
        int alIdx = 0;
        String dir = "acc";
        for(int i=0; i<s.length(); i++){
            String sub = s.substring(i,i+1);
            if(alIdx>=al.size() && alIdx<=numRows){
                al.add(new LinkedList<String>(Arrays.asList(sub)));
            }
            else{
                List l = al.get(alIdx);
                l.add(sub);
                // System.out.println(l);
                // System.out.println(alIdx);
            }

            if(numRows==1){
                alIdx=0;
            }
            else if(alIdx==numRows-1 && dir.equals("acc")){
                alIdx--;
                dir = "dec";
            }
            else if(alIdx==0 && dir.equals("dec")){
                alIdx++;
                dir = "acc";
            }
            else if(dir.equals("acc")){
                alIdx++;
            }
            else if(dir.equals("dec")){
                alIdx--;
            }
        }

        StringBuilder sb = new StringBuilder();
        for(int i=0; i<al.size(); i++){
            List l = al.get(i);
            while(l.size()>0){
                sb.append(l.remove(0));
            }
        }
        return sb.toString();
    }
}