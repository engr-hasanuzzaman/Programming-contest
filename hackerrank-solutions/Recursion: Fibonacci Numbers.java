import java.util.*;

public class Solution {    
    public static int fibonacci(int n) {
        // Complete the function.
        if(n < 2)
            return 1;
        
        int[] fibos = new int[n];       
        fibos[0] = 1;
        fibos[1] = 1;

        for(int i = 2; i < n; i++){
            fibos[i] = fibos[i - 1] + fibos[i - 2];
        }
        
        return fibos[n-1];
    }
    

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();
        System.out.println(fibonacci(n));
    }
}
