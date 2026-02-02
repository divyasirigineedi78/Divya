import java.util.Scanner;

class Armstrong {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), temp = n, sum = 0;

        while(temp != 0){
            int r = temp % 10;
            sum += r * r * r; // for 3-digit
            temp /= 10;
        }

        if(sum == n)
            System.out.println("Armstrong");
        else
            System.out.println("Not Armstrong");
    }
}
