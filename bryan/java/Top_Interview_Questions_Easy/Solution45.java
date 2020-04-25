package leetcode.tiq.easy.java;

public class Solution45 {
    public int hammingDistance(int x, int y) {
        String xstr = Integer.toString(x, 2);
        String ystr = Integer.toString(y, 2);

        int longer = xstr.length() > ystr.length() ? xstr.length() : ystr.length();

        String xpadstr = String.format("%" + longer + "s", xstr).replaceAll(" ", "0");
        String ypadstr = String.format("%" + longer + "s", ystr).replaceAll(" ", "0");

        int dist = 0;
        for (int i = 0; i < longer; i++) {
            if (xpadstr.charAt(i) != ypadstr.charAt(i)) {
                dist++;
            }
        }

        return dist;
    }
}
