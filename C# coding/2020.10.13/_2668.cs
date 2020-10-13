using System;
using System.Collections.Generic;

namespace _2668
{
    class _2668
    {
        static int n;
        static int[] arr;
        static List<List<int>> list = new List<List<int>>();
        static List<int> result = new List<int>();
        static void dfs(int v, int i, bool[] check)
        {
            check[v] = true;
            foreach (var j in list[v])
            {
                if (check[j] == false)
                {
                    dfs(j, i, check);
                }
                else if (check[j] && j == i)
                {
                    result.Add(j);
                }
            }
        }
        static void Main(string[] args)
        {
            n = int.Parse(Console.ReadLine());
            arr = new int[n + 1];
            for (int i = 0; i < n + 1; i++)
            {
                list.Add(new List<int>());
            }
            for (int i = 0; i < n; i++)
            {
                int a = int.Parse(Console.ReadLine());
                list[i+1].Add( a );
            }
            
            for (int i = 1; i < n + 1; i++)
            {
                bool[] check = new bool[n + 1];
                dfs(i, i, check);
            }
            Console.WriteLine(result.Count);
            foreach (int i in result)
            {
                Console.WriteLine(i);
            }
        }
    }
}
