package app;

import java.util.HashMap;
import java.util.Scanner;
import java.util.Stack;

class Solution20 {
    
    public static void main(String[] args) throws Exception {
        Scanner sc = null;
        sc = new Scanner(System.in);
        Solution20 s20 = new Solution20();
        boolean ans = s20.isValid_stack(sc.nextLine());
        //boolean ans = isValid(sc.nextLine());
        System.out.println(ans);
        sc.close();
    }

    // 自分の解答
    public static boolean isValid(String s) {
        String[] brackets = new String[] { "()", "[]", "{}" };
        String[] symbols = new String[] { "(", "[", "{" };

        // 文字数が奇数の場合はfalse
        if (s.length() % 2 != 0) {
            return false;
        }

        // 最も多い文字数の算出
        String workStr = s;
        int maxCount = 0;
        int workCount = 0;
        for (int i = 0; i < symbols.length; i++) {
            workStr = workStr.replace(symbols[i], "");
            workCount = s.length() - workStr.length();
            maxCount += workCount;
            workStr = s;
        }

        // 最大入れ子の回数分、括弧を削除
        for (int j = 0; j < maxCount; j++) {
            for (int k = 0; k < brackets.length; k++) {
                if (s.contains(brackets[k])) {
                    s = s.replace(brackets[k], "");
                }
            }
        }

        // 全て削除された場合、有効と判定
        if (s.length() == 0) {
            return true;
        }

        return false;
    }

    // 同アプローチの模範解答：計算量O(N^2)
    public static boolean isValid_answer(String s) {
        int length;

        do {
            length = s.length();
            s = s.replace("()", "").replace("{}", "").replace("[]", "");
        } while (length != s.length());

        return s.length() == 0;
    }

    // stackを使用した解答：計算量O(N)
    // Hash table that takes care of the mappings.
    private HashMap<Character, Character> mappings;

    // Initialize hash map with mappings. This simply makes the code easier to read.
    public Solution20() {
        this.mappings = new HashMap<Character, Character>();
        this.mappings.put(')', '(');
        this.mappings.put('}', '{');
        this.mappings.put(']', '[');
    }

    public boolean isValid_stack(String s) {

        //アルゴリズムで使用するスタックを初期化します
        Stack<Character> stack = new Stack<Character>();
    
        for (int i = 0; i < s.length(); i++) {
          char c = s.charAt(i);
    
          //現在の文字が閉じ括弧である場合
          if (this.mappings.containsKey(c)) {
    
            // スタックの一番上の要素を取得します。スタックが空の場合は、ダミー値「＃」を設定します
            char topElement = stack.empty() ? '#' : stack.pop();
    
            // このブラケットのマッピングがスタックの最上位要素と一致しない場合は、falseを返します
            if (topElement != this.mappings.get(c)) {
              return false;
            }
          } else {
            // 開始ブラケットの場合は、スタックに押し込みます
            stack.push(c);
          }
        }
    
        // スタックにまだ要素が含まれている場合、それは無効な式です
        return stack.isEmpty();
      }
}