package leetcode.tiq.easy.java;

public class Solution42 {

    public boolean isPowerOfThree(int n) {
        return Integer.toString(n, 3).matches("^10*$");
    }
}
