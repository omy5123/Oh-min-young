using System;
using System.Collections.Generic;

namespace _1249__swea_보급로_
{
    class _1249
    {
        static void bfs(int i, int j, int n, int m, int[,] arr, int[,] visit)
        {
            int[] dx = { -1, 1, 0, 0 };
            int[] dy = { 0, 0, 1, -1 };
            visit[i, j] = 0;
            Queue<(int, int)> que = new Queue<(int, int)>();
            que.Enqueue((i, j));
            while (que.Count != 0)
            {
                (int a, int b) = que.Dequeue();
                for (int k = 0; k < 4; k++)
                {
                    int x = a + dx[k];
                    int y = b + dy[k];
                    if ((0 <= x && x < n) && (0 <= y && y < m))
                    {
                        if (visit[x, y] == -1)
                        {
                            visit[x, y] = arr[x, y] + visit[a, b];
                            que.Enqueue((x, y));
                        }
                        else
                        {
                            if (visit[x, y] > arr[x, y] + visit[a, b])
                            {
                                visit[x, y] = arr[x, y] + visit[a, b];
                                que.Enqueue((x, y));
                            }
                            else
                            {
                                continue;
                            }
                        }
                    }
                }
            }
        }

        static void Main(string[] args)
        {
            string[] nm = Console.ReadLine().Split();
            int n = int.Parse(nm[0]);
            int m = int.Parse(nm[1]);
            int[,] arr = new int[n, m];
            int[,] visit = new int[n, m];
            for (int i = 0; i < n; i++)
            {
                string str = Console.ReadLine();
                for (int j = 0; j < m; j++)
                {
                    arr[i, j] = int.Parse(str[j].ToString());
                }
            }
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    visit[i, j] = -1;
                }
            }
            bfs(0, 0, n, m, arr, visit);
            Console.WriteLine(visit[n - 1, m - 1]);
        }
    }
}
