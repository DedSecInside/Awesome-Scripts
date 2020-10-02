//link to problem https://www.hackerrank.com/challenges/service-lane/problem

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class ServiceLane {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int t = in.nextInt();
        int width[] = new int[n];
        for(int width_i=0; width_i < n; width_i++){
            width[width_i] = in.nextInt();
        }
        int min=0;
        for(int a0 = 0; a0 < t; a0++){
            int i = in.nextInt();
            int j = in.nextInt();
            for(int k=i;k<=j;k++)
            {
                min=width[i];
                for(int l=i+1;l<=j;l++)
                {
                    if(width[l]<min)
                        min=width[l];
                }
            }
            System.out.println(min);
        }
    }
}
