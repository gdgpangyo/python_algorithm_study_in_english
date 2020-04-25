package leetcode.tiq.easy.java;

import java.util.ArrayList;
import java.util.List;

public class Solution39 {

    private List<Integer> stack;

    /** initialize your data structure here. */
    public Solution39() {
        stack = new ArrayList<>();
    }

    public void push(int x) {
        stack.add(x);
    }

    public void pop() {
        int lastIdx = stack.size() - 1;
        stack.remove(lastIdx);
    }

    public int top() {
        int lastIdx = stack.size() - 1;
        return stack.get(lastIdx);
    }

    public int getMin() {
        return stack.stream()
                .mapToInt(Integer::intValue)
                .reduce(Integer::min).getAsInt();
    }
}
