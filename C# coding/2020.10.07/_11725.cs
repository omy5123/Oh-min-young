using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace _11725__트리의_부모_찾기_
{
    class _11725
    {
        static List<List<int>> list = new List<List<int>>();
        static StringBuilder sb = new StringBuilder();
        static void dfs(int start, int[] parents)
        {
            foreach (int i in list[start])
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
            for (int i = 0; i < n + 1; i++)
            {
                list.Add(new List<int>());
            }
            for (int i = 0; i < n - 1; i++)
            {
                string[] line = Console.ReadLine().Split();
                int a = int.Parse(line[0]);
                int b = int.Parse(line[1]);
                list[a].Add(b);
                list[b].Add(a);
            }
            int[] parents = new int[n + 1];
            dfs(1, parents);
            for (int i = 2; i < n + 1; i++)
            {
                sb.Append(parents[i]).AppendLine();
            }
            Console.WriteLine(sb);
        }
    }
}
