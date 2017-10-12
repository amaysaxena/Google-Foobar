class Answer {

    public static int answer(String s) {
        int numForward = 0;
        int numSalutes = 0;

        char[] corridor = s.toCharArray();
        for (char x : corridor) {
            switch (x) {
                case '>':
                    numForward += 1;
                    break;
                case '<':
                    numSalutes += (2 * numForward);
                    break;
                case '-':
                    break;
            }
        }
        return numSalutes;
    }

    public static void main(String[] args) {
        //Tests
        String s1 = ">----<";
        System.out.println(answer(s1));

        String s2 = "<<>><";
        System.out.println(answer(s2));

        String s3 = "--->-><-><-->-";
        System.out.println(answer(s3));
    }
}
