class Solution
{
    //A method to check if the two strings are anagrams of each other
    public boolean isAnagram(String s, String t)
    {
        //Checks if the length of the two strings are equal
        if(s.length() != t.length())
        {
            return false;
        }

        //'a' (97) --> 'z' (122)
        int[] asciiCounter = new int[123];
        
        //A loop to increment each alphabet position in asciiCounter array
        for(int i = 0; i < s.length(); i++)
        {
            asciiCounter[(int)s.charAt(i)]++;
        }

        /*A loop to decrement each alphabet position filled in the previous loop.
            Ex) "racecar" ('a' --> 2 at index 97) -->
                "carrace" ('a' --> 2 - 2 = 0)*/
        for(int i = 0; i < t.length(); i++)
        {
            asciiCounter[(int)t.charAt(i)]--;

            //Returns false if any letters were found not in the first string
            if(asciiCounter[(int)t.charAt(i)] < 0)
            {
                return false;
            }
        }

        return true;
    }
}
