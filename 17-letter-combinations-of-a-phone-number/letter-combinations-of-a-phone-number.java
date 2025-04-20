class Solution {
    public List<String> letterCombinations(String digits) {
        Map<String,String> digM = new HashMap<>();
        digM.put("2","abc");
        digM.put("3","def");
        digM.put("4","ghi");
        digM.put("5","jkl");
        digM.put("6","mno");
        digM.put("7","pqrs");
        digM.put("8","tuv");
        digM.put("9","wxyz");

        List<String> res = new LinkedList<>();
        for(int i=0; i<digits.length(); i++){
            String letters = digM.get(digits.charAt(i)+"");
            if(res.size()==0){
                for(int j=0; j<letters.length(); j++){
                    res.add(letters.charAt(j)+"");
                }
            }
            else{
                int resL = res.size();
                List<String> resTemp = new LinkedList<>();
                for(int j=0; j<letters.length(); j++){
                    for(int k=0; k<resL; k++){
                        resTemp.add(res.get(k)+letters.charAt(j));
                    }
                }
                res = resTemp;
            }
        }

        return res;
    }
}