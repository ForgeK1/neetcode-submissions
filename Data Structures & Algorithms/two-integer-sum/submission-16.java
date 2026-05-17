class Solution
{
    public int[] twoSum(int[] nums, int target)
    {
        Map<Integer, Integer> map = new HashMap<>();

        /*A loop to add all numbers from nums to HashMap (in the loop below the 
          key-value pair is backwards on purpose)
            Ex) [Key -> Value] = [3 -> 0th index, 4 -> 1st index, 5 -> 2nd index]*/
        for(int i = 0; i < nums.length; i++)
        {
            map.put(nums[i], i);
        }

        /*A loop to iterate through each digit of nums, find its associated remainder
          to add up to the target, and return the index positions of the matching 
          numbers
            Ex) 7 - 3 = 4 -> We're looking for #4 in the HashMap*/
        for(int i = 0; i < nums.length; i++)
        {
            int remainder = target - nums[i];

            if(map.containsKey(remainder) && i != map.get(remainder))
            {
                return new int[] {i, map.get(remainder)};

                //Debug code
                    //System.out.println("Are you running?");
                    //System.out.println(i);
                    //System.out.println(map.get(remainder));
            }
        }

        return new int[] {};
    }
}