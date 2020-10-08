using System;
using System.Collections.Generic;
using System.IO;

namespace _11779__최소비용_구하기2_
{
    class _11779
    {
        static int n = 0;
        static int m = 0;
        static List<List<int[]>> list = new List<List<int[]>>();
        static int inf = int.MaxValue;
        
        static void dijkstra(int start, int end)
        {
            Queue<(int, int)> que = new Queue<(int, int)>();
            int[] dp = new int[n + 1];
            int[] visit = new int[n + 1];
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
                        visit[n_n] = b;
                        que.Enqueue((n_w, n_n));
                    }
                }
            }
            Console.WriteLine(dp[end]);
            Stack<int> stack = new Stack<int>();
            stack.Push(end);
            int tmp = visit[end];
            while (tmp != 0)
            {
                stack.Push(tmp);
                tmp = visit[tmp];
            }
            Console.WriteLine(stack.Count);
            Console.WriteLine(String.Join(" ", stack));

        }
        static void Main(string[] args)
        {
            n = int.Parse(Console.ReadLine());
            m = int.Parse(Console.ReadLine());
            for (int i = 0; i < n + 1; i++)
            {
                list.Add(new List<int[]>());
            }
            for (int i = 0; i < m; i++)
            {
                string[] line = Console.ReadLine().Split();
                int a = int.Parse(line[0]);
                int b = int.Parse(line[1]);
                int c = int.Parse(line[2]);
                list[a].Add(new int[] { b, c });
            }
            string[] se = Console.ReadLine().Split();
            int start = int.Parse(se[0]);
            int end = int.Parse(se[1]);
            dijkstra(start, end);
        }
    }
}
