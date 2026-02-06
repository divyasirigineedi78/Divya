import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        while (T-- > 0) {
            int temp = sc.nextInt();
            int humidity = sc.nextInt();

            if (temp >= 30 && humidity >= 90) {
                System.out.println("Hot and Humid");
            }
            else if (temp >= 30 && humidity < 90) {
                System.out.println("Hot");
            }
            else if (temp < 30 && humidity >= 90) {
                System.out.println("Cool and Humid");
            }
            else {
                System.out.println("Cool");
            }
        }
    }
}
