package Array;
import java.util.Arrays;

public class ArraySorting {
  public static void main(String[] args) {

      int[] org = {4, 2, 3, 1, 5};
      int[] sorted = soultion(org);
      System.out.println(Arrays.toString(org));
      System.out.println(Arrays.toString(sorted));

  }

  public static int[] soultion(int[] org) {
      int[] clone = org.clone();
      Arrays.sort(clone);
      return clone;
  }
}