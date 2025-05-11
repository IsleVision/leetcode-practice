class RandomizedSet {

    Set<Integer> s;

    public RandomizedSet() {
        s = new HashSet();
    }
    
    public boolean insert(int val) {
        return s.add(val);
    }
    
    public boolean remove(int val) {
        return s.remove(val);
    }
    
    public int getRandom() {
        Random rdm = new Random();
        int l = s.size();
        int i = rdm.nextInt(l);
        return (int)s.toArray()[i];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */