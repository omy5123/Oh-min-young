using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace _11725__트리의_부모_찾기_
{
    class _11725
    {
        static List<List<int>> arr = new List<List<int>>();
        static void dfs(int start, int [] parents)
        {
            foreach (int i in arr[start])
            {
                if (parents[i] == 0)
                {
                    parents[i] = start;
                    dfs(i, parents);
                }
            }
        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            for (int i = 0; i < n+1; i++)
            {
                arr.Add(new List<int>());
            }
            for (int i = 0; i < n-1; i++)
            {
                string[] st = Console.ReadLine().Split();
                int a = int.Parse(st[0]);
                int b = int.Parse(st[1]);
                arr[a].Add(b);
                arr[b].Add(a);
            }
            int[] parents = new int[n + 1];

            dfs(1,parents);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < parents.Length; i++)
            {
                sb.AppendLine(parents[i].ToString());
            }
            Console.WriteLine(sb);
        }
    }
}
