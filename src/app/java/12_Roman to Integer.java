package app;

import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;

class Solution12 {
    
    public static void main(String[] args) throws Exception {
        Scanner sc = null;
        sc = new Scanner(System.in);
        int ans = romanToInt(sc.nextLine());
        System.out.println(ans);
        sc.close();
    }

    //　自分の解答
    public static int romanToInt(String s) {
        int res = 0;
        Map<String, Integer> romanMap = new HashMap<String, Integer>();

        romanMap.put("I", 1);
        romanMap.put("V", 5);
        romanMap.put("X", 10);
        romanMap.put("L", 50);
        romanMap.put("C", 100);
        romanMap.put("D", 500);
        romanMap.put("M", 1000);

        Map<String, Integer> placeMap = new HashMap<String, Integer>();
        placeMap.put("IV", 4);
        placeMap.put("IX", 9);
        placeMap.put("XL", 40);
        placeMap.put("XC", 90);
        placeMap.put("CD", 400);
        placeMap.put("CM", 900);

        String workStr = s;

        for (Map.Entry<String, Integer> entry1 : placeMap.entrySet()) {
            if (s.contains(entry1.getKey())) {
                workStr = workStr.replace(entry1.getKey(), "");
                res += entry1.getValue() * ((s.length() - workStr.length()) / entry1.getKey().length());
                s = workStr;
            }
        }

        for (Map.Entry<String, Integer> entry2 : romanMap.entrySet()) {
            if (s.contains(entry2.getKey())) {
                workStr = workStr.replace(entry2.getKey(), "");
                res += entry2.getValue() * ((s.length() - workStr.length()) / entry2.getKey().length());
                s = workStr;
            }
        }

        return res;
    }
    
    //　模範解答
    public int romanToInt_answer(String s) {
        int num = 0;
        int l = s.length();
        int last = 1000;
        for (int i = 0; i < l; i++){
            int v = getValue(s.charAt(i));
            // 前の数値より大きかった場合、前の数値×２を引く
            // CMの場合、C:100 + M：1000 - C：100*2 =CM：900となる。
            if (v > last) num = num - last * 2;
            num = num + v;
            last = v;
        }
        return num;
    }
    private int getValue(char c){
        switch(c){
            case 'I' : return 1;
            case 'V' : return 5;
            case 'X' : return 10;
            case 'L' : return 50;
            case 'C' : return 100;
            case 'D' : return 500;
            case 'M' : return 1000;
            default : return 0;
        }
    }
}

