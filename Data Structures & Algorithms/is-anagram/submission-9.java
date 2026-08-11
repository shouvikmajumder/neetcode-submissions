class Solution {
    /*
        We are essentially just going to create 2 hashmaps and returning if they're equal or not

    */

    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> map_s = new HashMap<>();
        Map<Character, Integer> map_t = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            Character curr_char = s.charAt(i);

            if (!map_s.containsKey(curr_char)) {
                map_s.put(curr_char, 1);
            } else if (map_s.containsKey(curr_char)) {
                map_s.put(curr_char, map_s.get(curr_char) + 1);
            }
        }

        for (int i = 0; i < t.length(); i ++){
            char curr_char = t.charAt(i);
            if(!map_t.containsKey(curr_char)){
                map_t.put(curr_char, 1);
            }
            else if (map_t.containsKey(curr_char)){
                map_t.put(curr_char, map_t.get(curr_char) + 1);
            }
        }
        System.out.println(map_s);
        System.out.println(map_t);

        if (map_s.equals(map_t)){ 
            return true;
        }
        return false;
    }
}
