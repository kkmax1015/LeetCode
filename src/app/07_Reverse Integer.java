package app;

import java.util.Scanner;

class Solution7 {
    public static void main(String[] args) throws Exception {
        Scanner sc = null;
        sc = new Scanner(System.in);
        int ans = reverse(sc.nextInt());
        System.out.println(ans);
        sc.close();
    }

    public static int reverse(int x) {
        String strx = Integer.toString(x);
        String strRes = "";
        int res = 0;
        try {
            if(x >= 0){
                for(int i = 0; i < strx.length(); i++){
                    strRes = strx.substring(i,i+1) + strRes;
                }
                res = Integer.parseInt(strRes);
            } else {
                for (int i = 1; i < strx.length(); i++) {
                    strRes = strx.substring(i, i+1) + strRes;
                }
                res = Integer.parseInt(strRes) * -1;
            }         
        } catch (NumberFormatException e) {
            res = 0;
        }
        return res;
    }
}