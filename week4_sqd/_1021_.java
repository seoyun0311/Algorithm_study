import java.util.LinkedList;
import java.util.Scanner;

public class _1021_ {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        
        int N = sc.nextInt();
        int M = sc.nextInt();
      
        int[] positions = new int[M];
        for (int i = 0; i < M; i++) {
            positions[i] = sc.nextInt();
        }
        
        LinkedList<Integer> deque = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            deque.add(i);
        }
        
        int totalOperations = 0; 

        for (int i = 0; i < M; i++) {
            int target = positions[i];
            int targetIndex = deque.indexOf(target);
            int leftOperations = targetIndex;  
            int rightOperations = deque.size() - targetIndex;  
            
            if (leftOperations <= rightOperations) {
                for (int j = 0; j < leftOperations; j++) {
                    deque.addLast(deque.pollFirst());
                }
                totalOperations += leftOperations;
            } else {
            
                for (int j = 0; j < rightOperations; j++) {
                    deque.addFirst(deque.pollLast());
                }
                totalOperations += rightOperations;
            }
          
            deque.pollFirst();
        }
      
        System.out.println(totalOperations);
    }
}
