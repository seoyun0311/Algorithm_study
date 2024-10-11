import java.util.Scanner;
import java.util.Stack;

public class _1874_ {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] sequence = new int[n];
        
        for (int i = 0; i < n; i++) {
            sequence[i] = sc.nextInt();
        }

        Stack<Integer> stack = new Stack<>();
        StringBuilder result = new StringBuilder();
        int current = 1; // 스택에 넣을 값 (1부터 n까지)

        for (int i = 0; i < n; i++) {
            int target = sequence[i];

            // 스택에 값 넣기 (push)
            while (current <= target) {
                stack.push(current);
                result.append("+\n");
                current++;
            }

            // 스택에서 값 꺼내기 (pop)
            if (stack.peek() == target) {
                stack.pop();
                result.append("-\n");
            } else {
                System.out.println("NO");
                return;
            }
        }
        System.out.println(result.toString());
    }
}
