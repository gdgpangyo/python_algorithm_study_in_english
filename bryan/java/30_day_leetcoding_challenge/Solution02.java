import java.util.ArrayList;
import java.util.List;

public class Solution02 {

    private static final int LOOP_THRESHOLD = 100;

    public boolean isHappy(int n) {
        int count = 0;
        try {
            do {
                int sum = 0;
                List<Integer> elements = getElements(n);
                for (int i : elements) {
                    sum += Math.pow(i, 2);
                }
                n = sum;
                if (count++ > LOOP_THRESHOLD) throw new Exception();
            } while (n != 1);
        } catch (Exception e) {
            return false;
        }

        return true;
    }

    private List<Integer> getElements(int n) {
        List<Integer> elements = new ArrayList<>();

        while (n >= 10) {
            int remainder = n % 10;
            elements.add(remainder);
            n /= 10;
        }

        elements.add(n);
        return elements;
    }
}
