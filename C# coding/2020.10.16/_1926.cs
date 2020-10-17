using System;

namespace _1926__그림_
{
    class Program
    {
        static int n;
        static int m;
        static int[,] arr;
        static int[] dx = { -1, 1, 0, 0 };
        static int[] dy = { 0, 0, 1, -1 };
        static int cnt = 0;
        static int max = 0;
        static int count = 0;
        static void dfs(int i, int j)
        {
            arr[i, j] = 0;
            for (int k = 0; k < 4; k++)
            {
                int a = i + dx[k];
                int b = j + dy[k];
                if ((0 <= a && a < n) && (0 <= b && b < m) && arr[a, b] == 1)
                {
                    cnt += 1;
                    dfs(a, b);
                }
            }

        }
        static void Main(string[] args)
        {
            string[] nm = Console.ReadLine().Split();
            n = int.Parse(nm[0]);
            m = int.Parse(nm[1]);
            arr = new int[n, m];
            for (int i = 0; i < n; i++)
            {
                string[] line = Console.ReadLine().Split();
                for (int j = 0; j < m; j++)
                {
                    arr[i, j] = int.Parse(line[j]);
                }
            }
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    if (arr[i, j] == 1)
                    {
                        cnt = 1;
                        dfs(i, j);
                        count += 1;
                        max = Math.Max(max, cnt);
                    }
                }
            }
            Console.WriteLine(count);
            Console.WriteLine(max);
        }
    }
}
