package leetcode.tiq.easy.java;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Solution38 {

    private int[] nums;

    public Solution38(int[] nums) {
        this.nums = nums;
    }

    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return this.nums;
    }

    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        List<Integer> list = new ArrayList<>();
        for (int i : nums) {
            list.add(i);
        }

        Collections.shuffle(list);

        int[] shuffled = list.stream()
                .mapToInt(Integer::intValue)
                .toArray();

        return shuffled;
    }
}
