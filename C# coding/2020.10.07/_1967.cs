using System;
using System.Collections.Generic;
using System.Runtime.InteropServices.ComTypes;

namespace _1967__트리의_지름_
{
    class _1967
    {
        static List<List<int[]>> list = new List<List<int[]>>();
        static int n;
        static int inf = int.MaxValue;
        static int[] dijkstra(int start)
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
                    int n_w = wei + a;
                    if (n_w < dp[n_n])
                    {
                        dp[n_n] = n_w;
                        que.Enqueue((n_w, n_n));
                    }
                }
            }
            
            return dp;
        }
        static void Main(string[] args)
        {
            n = int.Parse(Console.ReadLine());
            for (int i = 0; i < n + 1; i++)
            {
                list.Add(new List<int[]>());
            }
            for (int i = 0; i < n - 1; i++)
            {
                string[] line = Console.ReadLine().Split();
                int a = int.Parse(line[0]);
                int b = int.Parse(line[1]);
                int c = int.Parse(line[2]);
                list[a].Add(new int[] { b, c });
                list[b].Add(new int[] { a, c });
            }
            
            int[] result =  dijkstra(1);

            int max = 0;
            for (int i = 1; i < n + 1; i++)
            {
                if (result[i] == inf)
                {
                    continue;
                }
                else
                {
                    if (result[i] > max)
                        max = result[i];
                }
            }
            int index = Array.IndexOf(result, max);
            int[] re = dijkstra(index);
            
            int m = 0;
            for (int i = 1; i < n + 1; i++)
            {
                if (re[i] == inf)
                {
                    continue;
                }
                else
                {
                    if (re[i] > m)
                        m = re[i];
                }
            }
            Console.WriteLine(m);
        }
    }
}
