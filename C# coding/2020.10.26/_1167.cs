using System;
using System.Collections.Generic;

namespace _1167__트리의_지름_
{
    class _1167
    {
        static int v;
        static int inf = int.MaxValue;
        static int[] dijkstra(int start, List<List<int[]>> list)
        {
            
            int[] dp = new int[v + 1];
            for (int j = 0; j < v+1; j++)
            {
                dp[j] = inf;
            }
            dp[start] = 0;
            Queue<(int, int)> que = new Queue<(int, int)>();
            que.Enqueue((0, start));
            while (que.Count != 0)
            {
                (int a, int b) = que.Dequeue();
                for (int k = 0; k < list[b].Count; k++)
                {
                    int n_n = list[b][k][0];
                    int n_w = list[b][k][1];
                    int wei = a + n_w;
                    if (wei < dp[n_n])
                    {
                        dp[n_n] = wei;
                        que.Enqueue((wei, n_n));
                    }
                }
            }
            
            return dp;
        }
        static void Main(string[] args)
        {
            v = int.Parse(Console.ReadLine());
            List<List<int[]>> list = new List<List<int[]>>();
            for (int i = 0; i < v; i++)
            {
                string[] line = Console.ReadLine().Split();
                int[] arr = new int[line.Length];
                for (int j = 0; j < line.Length; j++)
                {
                    arr[j] = int.Parse(line[j]); 
                }
                int idx = 1;
                int a = arr[0];
                for (int j = 0; j < v+1; j++)
                {
                    list.Add(new List<int[]>());
                }
                while(arr[idx] != -1)
                {
                    int b = arr[idx];
                    int c = arr[idx + 1];
                    list[a].Add(new int[] { b, c });
                    idx += 2;
                }
            }
            int max = 0;
            int[] result = dijkstra(1,list);
            for (int i = 1; i < v + 1; i++)
            {
                if (result[i] == inf)
                {
                    continue;
                }
                else
                {
                    max = Math.Max(max, result[i]);
                }
            }
            Console.WriteLine(string.Join(" ", result));
            int[] re = dijkstra(Array.IndexOf(result, max),list);
            int answer = 0;
            for (int i = 1; i < v + 1; i++)
            {
                if (result[i] == inf)
                {
                    continue;
                }
                else
                {
                    answer = Math.Max(answer, result[i]);
                }
            }
            Console.WriteLine(answer);
        }
    }
}
