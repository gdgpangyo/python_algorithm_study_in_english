package leetcode.tiq.easy.java;

import java.util.ArrayList;
import java.util.List;

public class Solution40 {

    private static final String CONST_FIZZ = "Fizz";
    private static final String CONST_BUZZ = "Buzz";

    public List<String> fizzBuzz(int n) {
        List<String> output = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            String res = "";

            if (i % 3 == 0 && i % 5 == 0) {
                res = CONST_FIZZ + CONST_BUZZ;
            } else if (i % 3 == 0) {
                res = CONST_FIZZ;
            } else if (i % 5 == 0) {
                res = CONST_BUZZ;
            } else {
                res = Integer.toString(i);
            }

            output.add(res);
        }

        return output;
    }
}
