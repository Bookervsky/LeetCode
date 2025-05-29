    class Solution {
        public int climbStairs(int n) {
            if (n == 1) return 1;
            int[] l = new int[n + 1];
            l[1] = 1;
            l[2] = 2;
            for (int i = 3; i <= n; i++) {
                l[i] = l[i - 1] + l[i - 2];
            }
            return l[n];
        }
    }