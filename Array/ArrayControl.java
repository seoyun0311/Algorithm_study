package Array;

import java.util.Arrays;
import java.util.Collections;

public class ArrayControl {
  public static int[] Soultion(int[] arr) {
    Integer[] result = Arrays.stream(arr).boxed().distinct().toArray(Integer[]::new);
    Arrays.sort(result, Collections.reverseOrder());
    return Arrays.stream(result).mapToInt(Integer::intValue).toArray();
  }
}
