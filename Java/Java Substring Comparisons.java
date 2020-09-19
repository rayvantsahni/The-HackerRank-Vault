import java.util.Scanner;

public class Solution {
    
    public static String getSmallestAndLargest(String s, int k) {

        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'

        int len = s.length();
        String[] arr = new String[len - k + 1];

        for (int i = 0; i < len - k + 1; i++)
        {
            String temp = "";
            for (int j = 0; j < k; j++)
                temp += s.charAt(i + j);

            arr[i] = temp;
        }

        java.util.Arrays.sort(arr);    

        String smallest = arr[0];
        String largest = arr[len - k];    

        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}
