class Solution 
{
    public boolean hasDuplicate(int[] nums) 
    {
        HashSet set = new HashSet();

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

        return false;
    }
}
