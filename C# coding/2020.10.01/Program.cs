using System;
using System.Collections.Generic;

namespace _2178__미로_탐색_
{
    class Program
    {
        static int n;
        static int m;
        static int bfs(int i, int j, int[,] arr)
        {
            Queue<(int, int)> que = new Queue<(int, int)>();
            int[] dx = { -1, 1, 0, 0 };
            int[] dy = { 0, 0, -1, 1 };
            que.Enqueue((i, j));
            while (que.Count != 0)
            {
                (int a, int b) = que.Dequeue();
                for (int k = 0; k < 4; k++)
                {
                    int x = a + dx[k];
                    int y = b + dy[k];
                    if ((0 <= x && x < n) && (0 <= y && y < m) && (arr[x, y] == 1))
                    {
                        que.Enqueue((x, y));
                        arr[x, y] = arr[a, b] + 1;
                    }
                }
            }
            return arr[n - 1, m - 1];
        }
        static void Main(string[] args)
        {
            string[] nm = Console.ReadLine().Split();
            n = int.Parse(nm[0]);
            m = int.Parse(nm[1]);

            int[,] arr = new int[n, m];
            for (int i = 0; i < n; i++)
            {
                string line = Console.ReadLine();
                for (int j = 0; j < line.Length; j++)
                {
                    arr[i, j] = int.Parse(line[j].ToString());
                }
            }
            
            Console.WriteLine(bfs(0, 0, arr));
        }
    }
}
