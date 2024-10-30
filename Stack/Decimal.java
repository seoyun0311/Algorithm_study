package Stack;
import java.util.Stack;

class Decimal {
  public static String Solution(int demcimal){
    Stack<Integer> stack = new Stack<>();
    
    while (decimal > 0){
      int remainder = decimal % 2;
      stack.push(remainder);
      decimal /= 2;
    }

    StringBuilder sb = new StringBuilder();
    while(!stack.isEmpty()){
      sb.append(stack.pop());
    }
  
  return sb.toString();
}
}