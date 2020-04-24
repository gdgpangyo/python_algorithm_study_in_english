package leetcode.tiq.easy.java;

import java.util.stream.IntStream;

public class Solution41 {

    public int countPrimes(int n) {
        return (int) IntStream.range(1, n)
                .filter(Solution41::isPrime)
                .count();
    }

    private static boolean isPrime(int n) {
        if (n <= 1) return false;
        return !IntStream.rangeClosed(2, n / 2).anyMatch(i -> n % i == 0);
    }
}
