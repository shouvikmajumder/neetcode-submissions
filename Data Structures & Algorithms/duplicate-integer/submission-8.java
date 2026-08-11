class Solution {
    public boolean hasDuplicate(int[] nums) {
        /*
            Problem Notes:
                just want to loop through the input array, store the outputs in another list and see if you encounter
                any element that appeared on that list
        */

        List<Integer> visited = new ArrayList<>();

        for (int i = 0; i < nums.length; i ++) { 
            int curr_num = nums[i];

            if (!visited.contains(curr_num)){ 
                visited.add(curr_num); 
            }  
            else if(visited.contains(curr_num)) {
                // Duplicate has been spotted  we can return true
                return true;
            }
        }

        return false;


    }
}