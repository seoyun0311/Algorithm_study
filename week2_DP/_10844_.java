import java.util.Scanner;

public class _10844_ {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int MOD = 1000000000;
        
        long[][] dp = new long[N + 1][10]; // dp[n][d] = 길이가 n, 마지막 숫자가 d인 계단 수의 개수
        
        for (int i = 1; i <= 9; i++) {
            dp[1][i] = 1; 
        }
        for (int n = 2; n <= N; n++) {
            for (int d = 0; d <= 9; d++) {
                if (d > 0) {
                    dp[n][d] += dp[n-1][d-1];  
                }
                if (d < 9) {
                    dp[n][d] += dp[n-1][d+1]; 
                }
                dp[n][d] %= MOD; 
            }
        }

        // 길이가 N인 계단 수의 합
        long result = 0;
        for (int d = 0; d <= 9; d++) {
            result += dp[N][d];
        }
        System.out.println(result % MOD);
    }
}
