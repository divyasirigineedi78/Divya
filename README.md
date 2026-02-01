import java.util.Scanner;
class Main
{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        char ch=sc.next().charAt(0);
        if(ch>='0'&&ch<='9')
        System.out.print("digit");
       else if(ch>='a'&&ch<='z'||ch>='A'&&ch<='Z')
        System.out.print("character");
        else
        System.out.print("not a char not a digit");
    }
    
}
    
