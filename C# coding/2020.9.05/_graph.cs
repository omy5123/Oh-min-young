using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata.Ecma335;

namespace _graph
{
    class _graph
    {
        static List<List<int[]>> arr = new List<List<int[]>>();
        static int inf = int.MaxValue;
        static int n = 6;
        static int solution(int n, int[,] edge)
        {
            for (int i = 0; i <= edge.Length / 2; i++)
            {
                arr.Add(new List<int []>());
            }
            for (int i = 0; i < edge.Length / 2; i++)
            {
                arr[edge[i,0]].Add(new int[] { edge[i, 1], 1 });
                arr[edge[i,1]].Add(new int[] { edge[i, 0], 1 });
            }
            
            int answer = dijkstra(1);
            Console.WriteLine(answer);
            return answer;
        }
        static int dijkstra(int start)
        {
            Queue<(int,int)> que = new Queue<(int,int)>();
            int[] dp = new int[n+1];
            for (int i = 0; i < n+1; i++)
            {
                dp[i] = inf;
            }
            dp[start] = 0;
            que.Enqueue((0, start));
            while (que.Count!=0)
            {
                (int a, int b) = que.Dequeue();
                for (int i = 0; i < arr[b].Count; i++)
                {
                    int n_n = arr[b][i][0];
                    int wei = arr[b][i][1];
                    int n_w = wei + a;
                    if (n_w < dp[n_n])
                    {
                        dp[n_n] = n_w;
                        que.Enqueue((n_w, n_n));
                    }
                }
                
            }
            int max = 0;
            for (int i = 1; i < dp.Length; i++)
            {
                if (dp[i] == inf)
                {
                    continue;
                }
                if (max < dp[i])
                {
                    max = dp[i];
                }
            }
            int cnt = 0;
            for (int i = 1; i < dp.Length; i++)
            {
                if (dp[i] == max)
                {
                    cnt += 1;
                }
            }
            return cnt;
        }
        static void Main(string[] args)
        {
            
            int[,] vertex = { { 3, 6 }, { 4, 3 }, { 3, 2 }, { 1, 3 }, { 1, 2 }, { 2, 4 }};
            solution(n, vertex);
        }
    }
}
