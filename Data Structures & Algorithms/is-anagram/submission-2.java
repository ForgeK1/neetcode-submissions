class Solution 
{
    public boolean isAnagram(String s, String t) 
    {
        /*If statement checks if lengths of both strings are equal. If they are not, that 
        indicates that both strings do not contain the exact same characters as another 
        string*/
        if(s.length() != t.length())
        {
            return false;
        }

        /*----------- METHOD 1 (Sorting) -----------*/

        //Creates two arrays based off of every character from their respective strings
        //String[] sArray = new String[s.length()];
        //String[] tArray = new String[t.length()];

        //for(int i = 0; i < s.length(); i++)
        //{
            //sArray[i] = s.charAt(i) + "";
            //tArray[i] = t.charAt(i) + "";
        //}

        /*Sorts both String arrays usign merge sort
            Ex) s = [r,a,c,e,c,a,r] & t = [c,a,r,r,a,c,e]

                s = [a,a,c,c,e,r,r] & t = [a,a,c,c,e,r,r]*/
        //mergeSort(sArray);
        //mergeSort(tArray);

        //Compares every String character with the other
        //for(int i = 0; i < sArray.length; i++)
        //{
            /*If one of the characters are not equal, that indicates that an anagram
            does not exist and we return false*/
            //if(sArray[i].compareTo(tArray[i]) != 0)
            //{
                //return false;
            //}
        //}

        /*----------- METHOD 2 (HashMap - Better Method) -----------*/
    
        HashMap<String, Integer> sH = new HashMap<String, Integer>();
        HashMap<String, Integer> tH = new HashMap<String, Integer>();

        for(int i = 0; i < s.length(); i++)
        {
            //Debug code
                //System.out.println("For loop runs");

            if(sH.containsKey(s.charAt(i) + ""))
            {
                sH.replace(s.charAt(i) + "", sH.get(s.charAt(i) + "") + 1);
            }
            else
            {
                sH.put(s.charAt(i) + "", 1);
            }

            if(tH.containsKey(t.charAt(i) + ""))
            {
                tH.replace(t.charAt(i) + "", tH.get(t.charAt(i) + "") + 1);
            }
            else
            {
                tH.put(t.charAt(i) + "", 1);
            }         
        }

        //Debug code
            //System.out.println(sH + "\n");
            //System.out.println(tH);
        
        for(Map.Entry<String, Integer> entry : sH.entrySet())
        {
            if(entry.getValue() != tH.get(entry.getKey()))
            {
                return false;
            }
        }

        return true;
    }

    /*----------- PART OF METHOD 1 (Sorting) -----------*/
    /*A sorting algorithm to keep breaking down the array into half of itself, sorting the values, and then
      putting the values back together into the original array*/
    public void mergeSort(String[] stringArray)
    {
        //Debug code
            //System.out.println("Merge sort method ran");

        //Checks if the array is down to only one element, if so then the array isn't broken down into two
        if(stringArray.length > 1)
        {
            //Ex) Array Length = 7, midIndex = (7 - 1) / 2 = 6 / 2 = 3
            int midIndex = (stringArray.length - 1) / 2;
            int leftIndex = 0;
            int rightIndex = 0;

            String[] leftArray = new String[midIndex + 1]; //Grabs elements 0, 1, 2, 3
            String[] rightArray = new String[stringArray.length - (midIndex + 1)]; //Grabs elements 4, 5, 6

            //A for loop to fill in the left and right array from the result array based on middle index
            for(int i = 0; i < stringArray.length; i++)
            {
                //Debug code
                    //System.out.println(stringArray.length + ", " + midIndex + ", " + i);

                if(i <= midIndex)
                {
                    leftArray[leftIndex] = stringArray[i];
                    leftIndex++;
                }
                else
                {
                    rightArray[rightIndex] = stringArray[i];
                    rightIndex++;
                }
            }

            //Uses recursion to break down the array in two again (Ex. 12 / 2 -> 6 / 2 -> 3 / 2 -> 1)
            mergeSort(leftArray);
            mergeSort(rightArray);

            /*Recursivly merges left and right array starting from the point where both arrays have 
              only one element*/
            merge(leftArray, rightArray, stringArray);
        }
    }

    /*----------- PART OF METHOD 1 (Sorting) -----------*/
    //A helper method to sort and merge two arrays back together
    public void merge(String[] leftArray, String[] rightArray, String[] result)
    {
        //Debug code
            //System.out.println("Merge method ran");

        int leftIndex = 0;
        int rightIndex = 0;
        int resultIndex = 0;

        /*A while loop to compare values from the left and right array, and whichever is higher in
          each comparison, that value is put into the result array*/
        while(resultIndex != result.length)
        {
            //Debug code
                //System.out.println(leftIndex + ", " + rightIndex + ", " + resultIndex);
            
            /*Case 1: All values from the left array have been added to the result array, so now the 
                      rest of the values from the right array is added to the result array*/
            if(leftIndex == leftArray.length)
            {
                for(int i = rightIndex; i < rightArray.length; i++)
                {
                    result[resultIndex] = rightArray[i];

                    resultIndex++;
                }

                break;
            }
            
            /*Case 1: All values from the righ array have been added to the result array, so now the 
                      rest of the values from the left array is added to the result array*/
            if(rightIndex == rightArray.length)
            {
                for(int i = leftIndex; i < leftArray.length; i++)
                {
                    result[resultIndex] = leftArray[i];

                    resultIndex++;
                }

                break;
            }

            //Case 3: Compares every left array value to every right array value to add to the result array
            if(leftArray[leftIndex].compareTo(rightArray[rightIndex]) > 0)
            {
                result[resultIndex] = leftArray[leftIndex];

                leftIndex++;
                resultIndex++;
            }
            else
            {
                result[resultIndex] = rightArray[rightIndex];

                rightIndex++;
                resultIndex++;
            }
        }
    }
}
