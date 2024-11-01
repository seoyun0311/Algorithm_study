package Hash;
import java.util.HashMap;

public class Discount {
  public int discount(String[] want, int[] number, String[] discount){
    HashMap<String,Integer> wantMap = new HashMap<>();
    for(int i = 0; i < want.length; i++){
      wantMap.put(want[i], number[i]);
    }
    int answer = 0;
    for(int i = 0; i < discount.length; i++){
      HashMap<String, Integer> discountmap = new HashMap<>();

      for(int j = 0; j < i + 10; j++){
        if(wantMap.containsKey(discount[j])){
          discountmap.put(discount[j], discountmap.getOrDefault(discount[j], 0) + 1);
        }
      }
      if(discountmap.equals(wantMap))
        answer++;
    }
    return answer;
  }
  
}
