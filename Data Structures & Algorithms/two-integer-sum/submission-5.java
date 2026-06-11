class Solution 
{
    public int[] twoSum(int[] nums, int target) 
    {
        int i = 0;
        int j = nums.length - 1;

        while(i != j)
        {
            int result = nums[i] + nums[j];
            int target2 = target;

            //Converts result and target to positive integers before comparison
            if(result < 0 && target < 0)
            {
                result = result * -1;
                target2 = target2 * -1;
            }

            int posResult = result * -1;
            int posTarget = target * -1;

            System.out.println(result);
            System.out.println(target2 + "\n");

            if(result == target2)
            {
                return new int[]{i, j};                
            }
            else if(result < target2)
            {
                i++;
            }
            else if(result > target2)
            {
                j--;
            }
        }

        return null;
    }
}
