import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        
        StringBuffer a = new StringBuffer(A);
        a = a.reverse();
        System.out.println(a.toString().equals(A) ? "Yes" : "No");
    }
}
