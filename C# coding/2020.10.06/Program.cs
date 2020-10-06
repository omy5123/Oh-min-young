using System;

namespace _2606__바이러스_
{
    class Program
    {
        static int[,] arr;
        static int n;
        static int m;
        static bool[] visit;
        static int cnt = 0;
        static void dfs(int start)
        {
            for (int i = 1; i < n+1; i++)
            {
                if (arr[start, i] == 1 && visit[i] == false)
                {
                    visit[i] = true;
                    cnt += 1;
                    dfs(i);
                }
            }
        }
        static void Main(string[] args)
        {
            n = int.Parse(Console.ReadLine());
            m = int.Parse(Console.ReadLine());
            
            arr = new int[n + 1, n + 1];
            visit = new bool[n + 1];
            for (int i = 0; i < m; i++)
            {
                string[] line = Console.ReadLine().Split();
                int a = int.Parse(line[0]);
                int b = int.Parse(line[1]);
                arr[a, b] = 1;
                arr[b, a] = 1;
            }
            
            dfs(1);
            if (cnt == 0)
            {
                Console.WriteLine(cnt);
            }
            else
            {
                Console.WriteLine(cnt-1);
            }

        }
    }
}
