import java.util.Scanner;

public class _11057_ {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int MOD = 10007;

        int[][] dp = new int[N+1][10];

        for (int i = 0; i <= 9; i++) {
            dp[1][i] = 1;
        }

        for (int i = 2; i <= N; i++) {
            for (int j = 0; j <= 9; j++) {
                dp[i][j] = 0;
                for (int k = 0; k <= j; k++) {
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD;
                }
            }
        }

        int result = 0;
        for (int i = 0; i <= 9; i++) {
            result = (result + dp[N][i]) % MOD;
        }

        System.out.println(result);
    }
}
