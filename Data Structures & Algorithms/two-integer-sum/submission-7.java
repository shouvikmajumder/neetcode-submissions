class Solution {
    /*
        we can store the the value as a key and the index as the value in a hashmap
        every iteration we can check if the difference between the target and the current value that
        the pointer is on is in the hashmap, if it is you return the 2 indexs, otherwise you would
       just keep adding to the dict
    */

    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int idx = 0; idx < nums.length; idx++) {
            int currIdxVal = nums[idx];
            int difference = target - currIdxVal;

            if (map.containsKey(difference)) {
                // we want to return the indexes of these 2
                return new int[] {map.get(difference), idx};
            }
            // continue putting elements in the map
            map.put(currIdxVal, idx);
        }
        return new int[] {};
    }
}
