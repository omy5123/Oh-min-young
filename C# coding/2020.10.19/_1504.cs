using System;
using System.Collections.Generic;

namespace _1504__특정한_최단_경로_
{
    class _1504
    {
        static int inf = int.MaxValue;
        static List<List<int[]>> list = new List<List<int[]>>();
        static int[] dijkstra(int start, int n, int e)
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
                    int n_w = list[b][i][1];
                    int wei = a + n_w;
                    if (wei < dp[n_n])
                    {
                        dp[n_n] = wei;
                        que.Enqueue((n_w, n_n));
                    }
                }

            }
            return dp;

        }

        static int solution(int n, int e, int[,] arr, int v1, int v2)
        {

            for (int i = 0; i <= arr.GetLength(0); i++)
            {
                list.Add(new List<int[]>());
            }
            for (int i = 0; i < arr.GetLength(0); i++)
            {
                list[arr[i, 0]].Add(new int[] { arr[i, 1], arr[i, 2] });
                list[arr[i, 1]].Add(new int[] { arr[i, 0], arr[i, 2] });
            }
            int[] one = dijkstra(1, n, e);
            int[] v_1 = dijkstra(v1, n, e);
            int[] v_2 = dijkstra(v2, n, e);
            Console.WriteLine(string.Join(" ", one));
            Console.WriteLine(string.Join(" ", v_1));
            Console.WriteLine(string.Join(" ", v_2));
            int min = Math.Min(one[v1] + v_1[v2] + v_2[n], one[v2] + v_2[v1] + v_1[n]);
            return min;
        }
        static void Main(string[] args)
        {
            int n = 4;
            int e = 6;

            int[,] arr = { { 1, 2, 3 }, { 2, 3, 3 }, { 3, 4, 1 }, { 1, 3, 5 }, { 2, 4, 5 }, { 1, 4, 4 } };
            int v1 = 2;
            int v2 = 3;
            Console.WriteLine(solution(n, e, arr, v1, v2));
        }
    }
}
