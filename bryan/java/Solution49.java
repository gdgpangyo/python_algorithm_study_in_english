package leetcode.tiq.easy.java;

public class Solution49 {

    public int missingNumber(int[] nums) {
        boolean[] exists = new boolean[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            exists[nums[i]] = true;
        }

        int idx = -1;
        for (int i = 0; i < nums.length + 1; i++) {
            if (!exists[i]) {
                idx = i;
                break;
            }
        }

        return idx;
    }
}
