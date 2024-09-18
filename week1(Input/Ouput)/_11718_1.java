import java.util.Scanner;

public class _11718_1 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    while (sc.hasNextLine()) { // 입력이 있는 동안 계속해서 처리
      String str = sc.nextLine(); // 입력을 한 줄씩 읽음
      System.out.println(str); 
    }

    sc.close();
}
}