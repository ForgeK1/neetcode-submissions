class Solution
{
    public int[] twoSum(int[] nums, int target)
    {
        //Declares an instance of a HashMap
        Map<Integer, Integer> map = new HashMap<>();

        /*A loop to add all numbers from nums to HashMap
            Ex) [Key -> Value] = [3 -> 0, 4 -> 1, 5 -> 2]*/
        for(int i = 0; i < nums.length; i++)
        {
            map.put(nums[i], i);
        }

        //A loop to 
        for(int i = 0; i < nums.length; i++)
        {
            //7 - 3 = 4 -> We're looking for #4 in the HashMap
            int remainder = target - nums[i];

            if(map.containsKey(remainder) && nums[i] != remainder)
            {
                System.out.println("Are you running?");
                System.out.println(i);
                System.out.println(map.get(remainder));

                return new int[] {i, map.get(remainder)};
            }
        }

        return new int[] {};
    }
}