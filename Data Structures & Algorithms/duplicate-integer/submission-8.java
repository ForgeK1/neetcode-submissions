class Solution 
{
    //A method to check for any duplicate values in an array
    public boolean hasDuplicate(int[] nums)
    {
        //Declares a HashSet
        HashSet set = new HashSet();

        /*Loops through each nums digit to check if it exists in the set. If
          the number already exists, then there is a duplicate. Else, the number
          gets added to the set*/
        for(int i = 0; i < nums.length; i++)
        {
            if(set.contains(nums[i]))
            {
                return true;
            }
            else
            {
                set.add(nums[i]);
            }
        }

        //Returns false if there isn't a duplicate value
        return false;
    }
}