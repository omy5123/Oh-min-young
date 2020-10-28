using System;
using System.Collections.Generic;

namespace _11048__이동하기_
{
    class _11048
    {
        static int[] dx = { 1,0 };
        static int[] dy = { 0,1 };
        static int n;
        static int m;
        static int inf = int.MaxValue;
        static void bfs(int i, int j, int[,] arr, int[,] visit)
        {
            visit[i, j] = arr[i,j];
            Queue<(int, int)> que = new Queue<(int, int)>();
            que.Enqueue((i, j));
            while (que.Count != 0)
            {
                (int a, int b) = que.Dequeue();
                for (int k = 0; k < 2; k++)
                {
                    int x = dx[k] + a;
                    int y = dy[k] + b;
                    if ((0 <= x && x < n) && (0 <= y && y < m))
                    {
                        if (visit[x, y] == inf)
                        {
                            visit[x, y] = visit[a, b] + arr[x, y];
                            que.Enqueue((x, y));
                        }
                        else
                        {
                            if (visit[x, y] < visit[a, b] + arr[x, y])
                            {
                                visit[x, y] = visit[a, b] + arr[x, y];
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
        static void solution(int n, int m, int[,] arr, int[,] visit)
        {
            bfs(0, 0, arr, visit);
        }
        static void Main(string[] args)
        {
            string[] nm = Console.ReadLine().Split();
            n = int.Parse(nm[0]);
            m = int.Parse(nm[1]);
            int[,] arr = new int[n, m];
            int[,] visit = new int[n, m];
            
            for (int i = 0; i < n; i++)
            {
                string[] line = Console.ReadLine().Split();
                for (int j = 0; j < m; j++)
                {
                    arr[i, j] = int.Parse(line[j]);
                    visit[i, j] = inf;
                }
            }
            solution(n, m, arr, visit);
            Console.WriteLine(visit[n - 1, m - 1]);
        }
    }
}
