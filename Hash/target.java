package Hash;

import java.util.HashSet;

public class target {
  private static boolean target(int[] arr, int target){
    HashSet<Integer> hashset = new HashSet<>();

    for(int i : arr)
    {
      if(hashset.contains(target - i)){
        return true;
      }
    hashset.add(i);
    }
    return false;

  }
  
}
