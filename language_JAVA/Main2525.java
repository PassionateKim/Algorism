package language_JAVA;

import java.util.Scanner;

public class Main2525 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int m = sc.nextInt();
        int value = sc.nextInt();

        m = m + value;
        while(m >= 60){
            m = m - 60;
            h = h + 1;
            if(h >= 24){
                h = h-24;
            }

        }
        System.out.println(h+" "+m);
    }
}
