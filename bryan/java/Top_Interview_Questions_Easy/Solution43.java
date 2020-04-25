package leetcode.tiq.easy.java;

public class Solution43 {

    private String[] roman2 = new String[]{"IV", "IX", "XL", "XC", "CD", "CM"};
    private String[] roman1 = new String[]{"I", "V", "X", "L", "C", "D", "M"};

    public int romanToInt(String s) {
        int res = 0;

        for (String r : roman2) {
            if (s.contains(r)) {
                s = s.replace(r, "");
                res += convert2Decimal(r);
            }
        }

        for (String r : roman1) {
            while(s.contains(r)) {
                s = s.replaceFirst(r, "");
                res += convert2Decimal(r);
            }
        }

        return res;
    }

    private int convert2Decimal(String roman) {
        switch (roman) {
            case "IV": return 4;
            case "IX": return 9;
            case "XL": return 40;
            case "XC": return 90;
            case "CD": return 400;
            case "CM": return 900;
            case "I": return 1;
            case "V": return 5;
            case "X": return 10;
            case "L": return 50;
            case "C": return 100;
            case "D": return 500;
            case "M": return 1000;
            default: return 0;
        }
    }
}
