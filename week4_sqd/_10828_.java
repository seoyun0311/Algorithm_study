package Algorithm_study.week4_sqd;

import java.util.Scanner;
import java.util.Stack;

public class _10828_ {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); 

        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < N; i++) {
            String command = sc.next(); 

            if (command.equals("push")) {
                int x = sc.nextInt();
                stack.push(x);
            } 
            
            else if (command.equals("pop")) {
                if (stack.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(stack.pop());
                }
            } 
            
            else if (command.equals("size")) {
                System.out.println(stack.size());
            } 
            
            else if (command.equals("empty")) {
                System.out.println(stack.isEmpty() ? 1 : 0);
            } 
            
            else if (command.equals("top")) {
                if (stack.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(stack.peek());
                }
            }
        }
        
        sc.close();
    }
}



