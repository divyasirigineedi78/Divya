import java.util.Scanner;

class ArraySum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter array size:");
        int n=sc.nextInt();
        System.out.print("enter array elements:");
        int arr[] = new int[n];
     for(int i=0;i<n;i++)
     arr[i]=sc.nextInt();
     System.out.print("reverse array:")
     for(i=n-1;i>=0;i--)
        System.out.println(arr[i]+" ");
    }
}
