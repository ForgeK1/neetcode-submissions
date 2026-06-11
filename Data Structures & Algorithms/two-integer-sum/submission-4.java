class Solution 
{
    public int[] twoSum(int[] nums, int target) 
    {
        int i = 0;
        int j = nums.length - 1;

        while(i != j)
        {
            int result = nums[i] + nums[j];

            System.out.println(result);

            //Converts result and target to positive integers before comparison
            if(result < 0 && target < 0)
            {
                result = result * -1;
                target = target * -1;
            }

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
