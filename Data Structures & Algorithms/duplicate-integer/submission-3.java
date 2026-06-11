class Solution 
{
    public boolean hasDuplicate(int[] nums)
    {
        //Use Counting Sort to sort the algorithm
        int[] sortedNums = countingSort(nums);

        //A for loop to compare each index value to the value of the neighboring index
        for(int i = 0; i < sortedNums.length - 1; i++)
        {
            //Returns true if there is a duplicate value
            if(sortedNums[i] == sortedNums[i + 1])
            {
                return true;
            }
        }

        //Returns false if there isn't a duplicate value
        return false;
    }

    public int[] countingSort(int[] nums)
    {
        //Creates array variables 
        int[] counts;
        int[] result = new int[nums.length];

        //Keeps track of the largest number in the nums array
        int countsLength = nums[0];

        for(int i = 1; i < nums.length; i++)
        {
            if(countsLength < nums[i])
            {
                countsLength = nums[i];
            }
        }
        
        //Instantiates the counts array based on countsLength
        counts = new int[countsLength + 1];

        //Fills in the counts array based on each digit of the nums array
        for(int i = 0; i < nums.length; i++)
        {
            counts[nums[i]] += 1;
        }

        //Adds each value from index position to the next for the counts array
        for(int i = 0; i < counts.length - 1; i++)
        {
            counts[i + 1] = counts[i] + counts[i + 1]; 
        }

        //Creates the result array based on the nums and counts arrays
        for(int i = nums.length - 1; i >= 0; i--)
        {
            //Grabs the index for the current nums value
            int index = counts[nums[i]] - 1;

            //Decrements value of the counts position used
            counts[nums[i]]--;

            //Utilizes the index to place the nums value in the correct position
            result[index] = nums[i];
        }

        System.out.println(toString(result));

        return result;
    }

    //A string method to return a String representation of the given array
    public String toString(int[] array)
    {
        String result = "[";

        for(int i = 0; i < array.length - 1; i++)
        {
            result += array[i] + ", ";
        }

        result += array[array.length - 1] + "]";

        return result;
    }
}