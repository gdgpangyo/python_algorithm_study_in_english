package leetcode.tiq.easy.java;

import java.util.ArrayList;
import java.util.List;

public class Solution47 {

    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> output = new ArrayList<>();
        for (int i = 0; i <= numRows; i++) {
            List<Integer> list = new ArrayList<>(i+1);

            for (int j = 0; j < i; j++) {
                if (j == 0) {
                    list.add(1);
                } else if (j == i - 1) {
                    list.add(1);
                } else {
                    list.add(output.get(i-1).get(j-1) + output.get(i-1).get(j));
                }
            }

            output.add(list);
        }

        return output.subList(1, output.size());
    }
}
