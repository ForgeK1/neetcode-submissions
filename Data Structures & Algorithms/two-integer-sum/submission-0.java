class Solution 
{
    public int[] twoSum(int[] nums, int target) 
    {
        int i = 0;
        int j = nums.length - 1;

        while(nums[i] != nums[j])
        {
            int result = nums[i] + nums[j];

            if(result == target)
            {
                return new int[]{i, j};                
            }
            else if(result < target)
            {
                i++;
            }
            else if(result > target)
            {
                j--;
            }
        }

        return null;
    }
}
