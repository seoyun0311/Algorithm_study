import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _11718_2 {
  
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
    // (System.in)을 문자 스트림으로 변환
    String str;

    while((str=br.readLine()) != null) { // 입력이 있는 동안 반복
      System.out.println(str);
    }
      
  }
}
