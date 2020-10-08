using System;
using System.Collections.Generic;
using System.Text;

namespace _1761__정점들의_거리_
{
    class _1761
    {
        static int n = 0;
        static int inf = int.MaxValue;
        static StringBuilder sb = new StringBuilder();
        static List<List<int[]>> list = new List<List<int[]>>();
        static void dijkstra(int start, int end)
        {
            Queue<(int, int)> que = new Queue<(int, int)>();
            int[] dp = new int[n + 1];
            for (int i = 0; i < n + 1; i++)
            {
                dp[i] = inf;
            }
            dp[start] = 0;
            que.Enqueue((0, start));
            while (que.Count != 0)
            {
                (int a, int b) = que.Dequeue();
                for (int i = 0; i < list[b].Count; i++)
                {
                    int n_n = list[b][i][0];
                    int wei = list[b][i][1];
                    int n_w = a + wei;
                    if (dp[n_n] > n_w)
                    {
                        dp[n_n] = n_w;
                        que.Enqueue((n_w, n_n));
                    }
                }
            }
            sb.Append(dp[end]).AppendLine();

        }
        static void Main(string[] args)
        {
            n = int.Parse(Console.ReadLine());
            for (int i = 0; i < n + 1; i++)
            {
                list.Add(new List<int[]>());
            }
            for (int i = 0; i < n-1; i++)
            {
                string[] line = Console.ReadLine().Split();
                int a = int.Parse(line[0]);
                int b = int.Parse(line[1]);
                int c = int.Parse(line[2]);
                list[a].Add(new int[] { b, c });
                list[b].Add(new int[] { a, c });
            }
            int m = int.Parse(Console.ReadLine());
            for (int i = 0; i < m; i++)
            {
                string[] line = Console.ReadLine().Split();
                int start = int.Parse(line[0]);
                int end = int.Parse(line[1]);
                dijkstra(start, end);
            }
            Console.WriteLine(sb);
        }
    }
}
