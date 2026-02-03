class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();   // number of test cases

        while (T-- > 0) {
            int l1 = sc.nextInt();
            int l2 = sc.nextInt();
            int l3 = sc.nextInt();

            if (l1 + l2 > l3 && l1 + l3 > l2 && l2 + l3 > l1) {
                System.out.println(l1 + l2 + l3); // circumference
            } else {
                System.out.println(-1);
            }
        }
    }
}
