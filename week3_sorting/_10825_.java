import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class _10825_ {
  
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    String[][] arr = new String[N][4];

    for(int i = 0; i < N; i++) {
      arr[i][0] = sc.next(); // 이름 n
      arr[i][1] = sc.next(); // 국어 x
      arr[i][2] = sc.next(); // 영어 y 
      arr[i][3] = sc.next(); // 수학 z
    }

    Arrays.sort(arr, new Comparator<String[]>() {
      @Override
      public int compare(String[] s1, String[] s2) {
        int xCompare = Integer.parseInt(s2[1]) - Integer.parseInt(s1[1]); // 국어 비교
        if (xCompare != 0) {
            return xCompare;
        }
        
        int yCompare = Integer.parseInt(s1[2]) - Integer.parseInt(s2[2]); // 영어 비교
        if (yCompare != 0) {
            return yCompare;
        }
        
        int zCompare = Integer.parseInt(s2[3]) - Integer.parseInt(s1[3]); // 수학 비교
        if (zCompare != 0) {
            return zCompare;
        }
        
        return s1[0].compareTo(s2[0]); // 이름 비교
      }
    
    });
    for (int i = 0; i < N; i++) {
      System.out.println(arr[i][0]);
    }
}
}