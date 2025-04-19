class Solution {
    public int evalRPN(String[] tokens) {
        List<Integer> opNums = new LinkedList<>();
        for(int i=0; i<tokens.length; i++){
            if(!"+".equals(tokens[i]) && 
            !"-".equals(tokens[i]) && 
            !"*".equals(tokens[i]) && 
            !"/".equals(tokens[i])){
                opNums.add(Integer.parseInt(tokens[i]));
            }
            else{
                int opNum2 = opNums.removeLast();
                int opNum1 = opNums.removeLast();
                int opRes=0;
                if("+".equals(tokens[i])){
                    opRes=opNum1+opNum2;
                }
                else if("-".equals(tokens[i])){
                    opRes=opNum1-opNum2;
                }
                else if("*".equals(tokens[i])){
                    opRes=opNum1*opNum2;
                }
                else if("/".equals(tokens[i])){
                    opRes=opNum1/opNum2;
                }
                opNums.add(opRes);
            }
        }
        return opNums.get(0);
    }
}