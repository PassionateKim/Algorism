package language_JAVA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int[][] graph;

    static int n;

    static int m;

    static int[] dx = new int[]{-1,1,0,0};
    static int[] dy = new int[]{0, 0, -1, 1};
    static int time = 0;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        String[] split = line.split(" ");
        n = Integer.parseInt(split[0]);
        m = Integer.parseInt(split[1]);
        time = Integer.parseInt(split[2]);

        graph = new int[n][m];

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < s.length(); j++) {

                if (s.charAt(j) == '.') {
                    graph[i][j] = -1;
                } else {
                    graph[i][j] = 3;
                }
            }
        }

        int checkTime = 0;
        boolean bombReady = true;

        while (checkTime < time) {
            // 다음 1초 동안 봄버맨은 아무것도 하지 않는다.
            if (checkTime == 0) {
                bombTimeDown();
                checkTime++;
                continue;
            }
            bombTimeDown();
            if (bombReady) {

                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < m; j++) {
                        // 다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다. 즉, 모든 칸은 폭탄을 가지고 있게 된다. 폭탄은 모두 동시에 설치했다고 가정한다.
                        if (graph[i][j] == -1) {
                            graph[i][j] = 3;
                        }
                    }
                }

                bombReady = false;
            } else {
                // 1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.

                Queue<int[]> readyBombList = new LinkedList<>();

                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < m; j++) {
                        if (graph[i][j] == 0) {
                            readyBombList.add(new int[]{i, j});
                        }
                    }
                }

                while (!readyBombList.isEmpty()) {
                    int[] poll = readyBombList.poll();
                    int x = poll[0];
                    int y = poll[1];

                    graph[x][y] = -1;

                    for (int idx = 0; idx < 4; idx++) {
                        int nx = x + dx[idx];
                        int ny = y + dy[idx];

                        if (!((0 <= nx && nx < n) && (0 <= ny && ny < m))) {
                            continue;
                        }
                        if (graph[nx][ny] != -1) {
                            graph[nx][ny] = -1;
                        }
                    }
                }

                bombReady = true;
            }

            checkTime++;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == -1) {
                    System.out.print('.');
                }
                else {
                    System.out.print('O');
                }
            }
            System.out.println();
        }
    }

    private static void bombTimeDown() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] != -1) {
                    graph[i][j] = graph[i][j] - 1;
                }
            }
        }
    }


}
