class Solution
{
    public boolean isAnagram(String s, String t)
    {
        if(s.length() != t.length())
        {
            return false;
        }

        //'a' (97) --> 'z' (122)
        int[] asciiCounter = new int[123];
        
        for(int i = 0; i < s.length(); i++)
        {
            asciiCounter[(int)s.charAt(i)]++;
        }

        for(int i = 0; i < t.length(); i++)
        {
            asciiCounter[(int)t.charAt(i)]--;

            if(asciiCounter[(int)t.charAt(i)] < 0)
            {
                return false;
            }
        }

        return true;
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
