import java.util.Scanner;
class Main
{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int r,s=0;
        int n=sc.nextInt();
        while(n!=0){//234
            r=n%10;//234%10=4
            s=s+r;//0+4=4
            n=n/10;//234/10=23
        }
        System.out.print("sum:"+s);
        
    }
}
