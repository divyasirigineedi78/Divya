import java.util.Scanner;
class SumOfArray
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int arr[]=new int[];
        int sum=0;
        for(i=1;i<=n;i++){
        arr[i]=sc.nextInt();
        sum+=arr[i];
        System.out.println("sum of array"+sum);
        }
  }
}
