import java.util.HashSet;
import java.util.Set;

class Fonkemon {
    public int solution(int[] nums) {
        int answer = 0;
        int count = nums.length / 2;
        Set<Integer> set = new HashSet<>(); 
        
        for(int num : nums){
            set.add(num); 
        }

        if(set.size() >= count){ 
            answer = count; 
        } else { 
            answer = set.size(); 
        }

        return answer;
    }
}