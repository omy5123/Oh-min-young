using System;

namespace _1937__욕심쟁이_판다_
{
    class _1937
    {
        static int n;
        static int[,] arr;
        static int[,] visit;
        static int[] dx = { -1, 1, 0, 0 };
        static int[] dy = { 0, 0, -1, 1 };

        static int dfs(int i, int j)
        {
            if(visit[i,j] < 0)
            {
                visit[i, j] = 0;
                for (int k = 0; k < 4; k++)
                {
                    int x = i + dx[k];
                    int y = j + dy[k];
                    if ((0 <= x && x < n) && (0 <= y && y < n) && (arr[i, j] < arr[x, y]))
                    {
                        visit[i, j] = Math.Max(visit[i, j], dfs(x, y));
                    }
                }
                visit[i, j] += 1;
            }
            return visit[i, j];
        }
        static void Main(string[] args)
        {
            n = int.Parse(Console.ReadLine());
            arr = new int[n, n];
            visit = new int[n,n];
            for (int i = 0; i < n; i++)
            {
                string[] line = Console.ReadLine().Split();
                for (int j = 0; j < n; j++)
                {
                    arr[i, j] = int.Parse(line[j].ToString());
                    visit[i, j] = -1;
                }
            }
            int k = int.MinValue;
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    k = Math.Max(k, dfs(i, j));
                }
            }
            Console.WriteLine(k);
        }
    }
}
