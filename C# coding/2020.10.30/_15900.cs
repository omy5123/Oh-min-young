using System;
using System.Collections.Generic;


namespace _15900__나무_탈출_
{
    class _15900
    {
        static long n;
        static List<List<int>> list = new List<List<int>>();
        static long depth = 0;
        static void dfs(int start, long[,]arr, long[] visit,int hei)
        {
            visit[start] = 1;
            bool isLeaf = true;
            for (int i = 0; i < list[start].Count; i++)
            {
                int a = list[start][i];
                if(visit[a] == 0)
                {
                    isLeaf = false;
                    dfs(a, arr, visit,hei+1);
                }
            }
            if(isLeaf)
            {
                depth += hei;
            }
        }
        static void Main(string[] args)
        {
            n = int.Parse(Console.ReadLine());
            long[,] arr = new long[n+1,n+1];
            for (int i = 0; i < n+1; i++)
            {
                list.Add(new List<int>());
            }
            for (int i = 0; i < n-1; i++)
            {
                string[] line = Console.ReadLine().Split();
                int a = int.Parse(line[0]);
                int b = int.Parse(line[1]);
                list[a].Add(b);
                list[b].Add(a);
            }
            long[] visit = new long[n + 1];
            dfs(1, arr,visit,0);
            
            if(depth % 2 == 0)
            {
                Console.WriteLine("No");
            }
            else
            {
                Console.WriteLine("Yes");
            }

        }
    }
}
