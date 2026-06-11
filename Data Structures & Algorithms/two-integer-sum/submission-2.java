class Solution 
{
    public int[] twoSum(int[] nums, int target) 
    {
        //An if statement to convert the target tp a positive number
        if(target < 0)
        {
            target = target * (-1);
        }

        //A for loop to convert each negative number to a positive number
        for(int i = 0; i < nums.length; i++)
        {
            if(nums[i] < 0)
            {
                nums[i] = nums[i] * (-1);
            }
        }

        int i = 0;
        int j = nums.length - 1;

        while(i != j)
        {
            int result = nums[i] + nums[j];

            System.out.println(result);

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
