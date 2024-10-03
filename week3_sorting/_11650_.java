import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class _11650_ {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    String[][] arr = new String[N][2];

    for (int i = 0; i < N; i++) {
      arr[i][0] = sc.next(); // x
      arr[i][1] = sc.next(); // y
    }

    Arrays.sort(arr, new Comparator<String[]>() {
      @Override
      public int compare(String[] s1, String[] s2) {
        int xCompare = Integer.parseInt(s1[0]) - Integer.parseInt(s2[0]); // x 비교
        if (xCompare != 0) {
          return xCompare;
        } else {
          return Integer.parseInt(s1[1]) - Integer.parseInt(s2[1]); // x가 같으면 y 비교
        }
      }
    });

    for (int i = 0; i < N; i++) {
      System.out.println(arr[i][0] + " " + arr[i][1]);
    }
  }
}
