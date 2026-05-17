class Solution 
{
    public boolean hasDuplicate(int[] nums) 
    {
        //Creates a HashSet
        Set<Integer> set = new HashSet<Integer>();
        
        /*A for loop to store each number in the set
            Case 1: The number is added if it doesn't exist in the set

            Case 2: If the number already exists after adding the previous
                    numbers, then there is a duplicate value 
        */
        for(int i = 0; i < nums.length; i++)
        {
            if(!set.contains(nums[i]))
            {
                set.add(nums[i]);
            }
            else
            {
                return true;
            }
        }

        //Returns false when all numbers were added to the set
        return false;
    }
}
