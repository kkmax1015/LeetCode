package app;

import java.util.Scanner;

class Solution9 {
    public static void main(String[] args) throws Exception {
        Scanner sc = null;
        sc = new Scanner(System.in);
        boolean ans = isPalindrome(sc.nextInt());
        System.out.println(ans);
        sc.close();
    }

    //　自分の解答
    public static boolean isPalindrome(int x) {
        boolean res = false;
        int work_x = x;
        long palNum = 0;

        if (x >= 0) {
            while (work_x != 0) {
                int pop = work_x % 10;
                work_x /= 10;
                palNum = palNum * 10 + pop;
            }

            if (x == palNum) {
                res = true;
            }
        }
        return res;
    }

    // 模範解答
    public static boolean isPalindrome_answer(int x) {

        if(x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int revertedNumber = 0;
        // 後半の数値の回文が前半の数値と一緒であることを確認するアプローチ
        // 元の数値を後半の回文が超えたら桁数の半分を処理したと判断
        // ex) 1221： 12 > 12でループ終了　1225： 12 > 52でループ終了　12345： 12 > 543でループ終了
        while (x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }
        
        return x == revertedNumber || x == revertedNumber/10;
    }
}