import java.util.Scanner;
class AlphabetOrNot{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter character:");
        char ch=sc.next().charAt(0);
        if(ch>='a'&&ch<='z'||ch>='A'&&ch<='Z')
        System.out.print("alphapet");
        System.out.print("not alphabet");
    }
}
    
