using System;
using System.Collections.Generic;

namespace _11438__LCA2_
{
    class _11438
    {
        static bool check = false;
        static void dfs_1(bool[] visit, int n, int m, int b, List<List<int>> list)
        {
            if (visit[b] == true)
            {
                Console.WriteLine(b);
                check = true;
                return;
            }
            for (int i = 0; i < list[b].Count; i++)
            {
                if (visit[list[b][i]] == false)
                {
                    dfs(visit, n, m, i, list);
                    if (check = true)
                    {
                        return;
                    }
                }
            }

        }
        static void dfs(bool[] visit, int n, int m, int a, List<List<int>> list)
        {
            visit[a] = true;
            for (int i = 0; i < list[a].Count; i++)
            {
                if (visit[list[a][i]] == false)
                {
                    dfs(visit, n, m, i, list);
                }
            }

        }
        static void solution(int n, int m, int[,] arr, int[,] brr)
        {
            List<List<int>> list = new List<List<int>>();
            for (int i = 0; i < n + 1; i++)
            {
                list.Add(new List<int>());
            }
            for (int i = 0; i < n; i++)
            {
                list[arr[i, 0]].Add(arr[i, 1]);
                list[arr[i, 1]].Add(arr[i, 0]);
            }
            for (int i = 0; i < m; i++)
            {
                bool[] visit = new bool[n + 1];
                int a = brr[i, 0];
                int b = brr[i, 1];
                dfs(visit, n, m, a, list);
                check = false;
                dfs(visit, n, m, b, list);

            }
        }




        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int[,] arr = new int[n, 2];
            for (int i = 0; i < n-1; i++)
            {
                string[] line = Console.ReadLine().Split();
                int a = int.Parse(line[0]);
                int b = int.Parse(line[1]);
                arr[i, 0] = a;
                arr[i, 1] = b;
            }

            int m = int.Parse(Console.ReadLine());
            int[,] brr = new int[m, 2];
            for (int i = 0; i < m; i++)
            {
                string[] line = Console.ReadLine().Split();
                int a = int.Parse(line[0]);
                int b = int.Parse(line[1]);
                brr[i, 0] = a;
                brr[i, 1] = b;
            }
            solution(n, m, arr, brr);
        }
    }
}
