import java.util.Arrays;


class Fonkemon {
  public int solution(int[] nums){
    return Math.min((int) Arrays.stream(nums).distinct().count(), nums.length / 2);
  }
   
}