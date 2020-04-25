import java.util.LinkedList;
import java.util.Queue;

public class Solution2nd17 {

    private final char ISLAND = '1';
    private final char WATER = '0';
    private final String DELIMITER = ",";

    private int row;
    private int col;


    public int numIslands(char[][] grid) {
        row = grid.length;
        col = grid[0].length;

        return numOfIsland(grid);
    }

    private int numOfIsland(char[][] v) {
        boolean[][] s = new boolean[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                s[i][j] = false;
            }
        }

        int count = 0;
        Queue<String> queue = new LinkedList<>();
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (!s[i][j] && v[i][j] == ISLAND) {
                    queue.add(i + DELIMITER + j);
                    bfs(queue, v, s);
                    count++;
                }
            }
        }

        return count;
    }

    private void bfs(Queue<String> queue, char[][] v, boolean[][] s) {
        while (queue.isEmpty() == false) {
            String x = queue.remove();
            int r = Integer.parseInt(x.split(DELIMITER)[0]);
            int c = Integer.parseInt(x.split(DELIMITER)[1]);

            if (isZero(r, c, v, s)) {
                continue;
            }

            s[r][c] = true;
            queue.add(r + DELIMITER + (c - 1));
            queue.add(r + DELIMITER + (c + 1));
            queue.add((r - 1) + DELIMITER + c);
            queue.add((r + 1) + DELIMITER + c);
        }
    }

    private boolean isZero(int r, int c, char[][] v, boolean[][] s) {
        return (r < 0 || c < 0 || r >= row || c >= col || s[r][c] || v[r][c] == WATER);
    }
}
