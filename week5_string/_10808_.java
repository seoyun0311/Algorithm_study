package Algorithm_study.week5_string;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _10808_ {
  public static void main(String[] args) throws IOException {
      BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
      
      int[] arr = new int[26];
      String s = br.readLine();

      for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        arr[c - 97]++;
      }

      for(int i = 0; i < 26; i++) {
        System.out.print(arr[i] + " ");
      }

  }
}
