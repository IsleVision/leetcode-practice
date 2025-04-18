class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new LinkedList<>();
        for(String s: strs){
            if(res.size()==0){
                res.add(new LinkedList<String>(Arrays.asList(s)));
            }
            else{
                boolean added = false;
                for(List<String> subList: res){
                    String ele = subList.get(0);
                    if(isAnagrams(ele,s)){
                        subList.add(s);
                        added = true;
                        break;
                    }
                }
                if(!added){
                    res.add(new LinkedList<String>(Arrays.asList(s)));
                }
            }
        }
        return res;
    }

    private boolean isAnagrams(String s1, String s2){
        StringBuilder sb2 = new StringBuilder(s2);
        if(s1==null || s2==null){
            return false;
        }
        else if(s1.length()!=sb2.length()){
            return false;
        }
        else{
            for(int i1=0; i1<s1.length(); i1++){
                int i2 = sb2.indexOf(s1.charAt(i1)+"");
                if(i2==-1){
                    return false;
                }
                else{
                    sb2.deleteCharAt(i2);
                }
            }
            if(sb2.length()==0){
                return true;
            }
            return false;
        }
    }
}