package app.java;

class Solution14 {
    
    public static void main(final String[] args) throws Exception {
        String[] strs = new String[] { "ca", "a" };
        String ans = longestCommonPrefix(strs);
        System.out.println(ans);
    }
    
    //　自分の解答
    public static String longestCommonPrefix(String[] strs) {
        String ans = "";
        String pfx = "";
        boolean empFlag = false;

        if (strs.length > 0) {
            pfx = strs[0];
        }

        for (int i = 1; i < strs.length; i++) {
            if (strs[i].isEmpty()) {
                empFlag = true;
                break;
            }
            for (int j = 0; j <= strs[0].length() - 1; j++) {
                if (strs[i].startsWith(pfx)) {
                    break;
                }
                pfx = pfx.substring(0, pfx.length() - 1);
            }
        }
        if (pfx.length() > 0 && empFlag == false) {
            ans = pfx;
        }
        return ans;
    }

    // 模範解答
    public static String longestCommonPrefix_answer(String[] strs) {
        if (strs == null || strs.length == 0) return "";    
            return longestCommonPrefix(strs, 0, strs.length - 1);
        }

        private static String longestCommonPrefix(String[] strs, int l, int r) {
        if (l == r) {
            return strs[l];
        }
        else {
            int mid = (l + r)/2;
            String lcpLeft =   longestCommonPrefix(strs, l , mid);
            String lcpRight =  longestCommonPrefix(strs, mid + 1,r);
            return commonPrefix(lcpLeft, lcpRight);
        }
    }
    
    static String commonPrefix(String left,String right) {
        int min = Math.min(left.length(), right.length());       
        for (int i = 0; i < min; i++) {
            if ( left.charAt(i) != right.charAt(i) )
                return left.substring(0, i);
        }
        return left.substring(0, min);
    }

}