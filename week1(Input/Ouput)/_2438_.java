import java.util.Scanner;
public class _2438_ {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 입력 받은 N 값

        for (int i = 1; i <= N; i++) { // 1부터 N까지 반복
          for (int j = 1; j <= i; j++) { // i번째 줄에 i개의 별 출력
            System.out.print("*");
          }
          System.out.println(); // 별 출력 후 줄 바꿈
        }
        sc.close();
    }
  
}