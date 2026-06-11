class Solution 
{
    public int[] twoSum(int[] nums, int target) 
    {
        int i = 0;
        int j = nums.length - 1;

        //Sorts the array before comparison

        while(i != j)
        {
            int posResult = nums[i] + nums[j];
            int posTarget = target;

            //Converts result and target to positive integers before comparison
            if(posResult < 0 && posTarget < 0)
            {
                posResult = posResult * -1;
                posTarget = posTarget * -1;
            }

            System.out.println(posResult);
            System.out.println(posTarget + "\n");

            if(posResult == posTarget)
            {
                return new int[]{i, j};                
            }
            else if(posResult < posTarget)
            {
                i++;
            }
            else if(posResult > posTarget)
            {
                j--;
            }
        }

        return null;
    }
}
