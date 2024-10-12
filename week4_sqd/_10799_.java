import java.util.Scanner;
import java.util.Stack;

public class _10799_ {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        
        Stack<Character> stack = new Stack<>();
        int result = 0; 
        
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            
            if (c == '(') {
                stack.push(c); // 여는 괄호면 스택에 넣음
            } else { 
                stack.pop(); // 닫는 괄호면 스택에서 하나를 꺼냄
                
                if (input.charAt(i - 1) == '(') {
                    result += stack.size(); // 현재 스택에 남아있는 쇠막대기만큼 자름
                } else {
                    // 그렇지 않으면 쇠막대기의 끝이므로 1개 조각이 추가
                    result += 1;
                }
            }
        }
        
        System.out.println(result);
    }
}
