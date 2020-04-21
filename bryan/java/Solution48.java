package leetcode.tiq.easy.java;

import java.util.Stack;

public class Solution48 {

    public boolean isValid(String s) {
        if (oddInput(s)) return false;
        if (closedFirstInput(s)) return false;

        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (isOpen(c)) {
                stack.push(c);
                continue;
            }

            if (stack.size() == 0) {
                continue;
            }

            char popped = stack.peek();
            if (isPair(c, popped)) {
                stack.pop();
                continue;
            } else {
                return false;
            }
        }

        if (stack.size() != 0) {
            return false;
        }

        return true;
    }

    private boolean closedFirstInput(String s) {
        if (s.length() != 0) {
            if (isClosed(s.charAt(0))) {
                return true;
            }
        }
        return false;
    }

    private boolean oddInput(String s) {
        if (s.length() % 2 == 1) {
            return true;
        }
        return false;
    }

    private boolean isClosed(char c) {
        if (c == ')' || c == '}' || c == ']') {
            return true;
        }

        return false;
    }

    private boolean isOpen(char c) {
        if (c == '(' || c == '{' || c == '[') {
            return true;
        }

        return false;
    }

    private boolean isPair(char a, char b) {
        if (a == ')' && b == '(') {
            return true;
        } else if (a == '}' && b == '{') {
            return true;
        } else if (a == ']' && b == '[') {
            return true;
        }

        return false;
    }
}
