import java.util.Scanner;

public class _2011_ {
  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      String code = sc.next();
      int MOD = 1000000;

      if (code.charAt(0) == '0') {
        System.out.println(0);
        return;
      }

      int n = code.length();
      int[] dp = new int [n + 1];
      dp[0] = 1;

      for (int i = 1; i <=n; i++) {
        int one = code.charAt(i - 1) - '0';
        if (one >= 1 && one <= 9) {
          dp[i] += dp[i-1];
          dp[i] %= MOD;
        }
        if (i > 1) {
          int two = (code.charAt(i - 2) - '0') * 10 + (code.charAt(i - 1) - '0');
          if (two >= 10 && two <= 26) {
            dp[i] += dp[i - 2];
            dp[i] %= MOD;
          }
        }
      }
      System.out.println(dp[n]);
      sc.close();
    }

}
