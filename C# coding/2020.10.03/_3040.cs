using System;
using System.Collections.Generic;
using System.Text;

namespace _3040__백설_공주와_일곱_난쟁이_
{
    class _3040
    {
        static List<int> list = new List<int>();
        static int[] arr;
        static bool check = false;
        static StringBuilder sb = new StringBuilder();
        static void dfs(int cnt, int sum, int idx)
        {
            if (cnt == 7)
            {
                if (sum == 100)
                {
                    sb.Append(string.Join("\n", list));
                    check = true;
                    return;
                }
            }
            else
            {
                for (int i = idx; i < 9; i++)
                {
                    list.Add(arr[i]);
                    dfs(cnt + 1, sum + arr[i], i + 1);
                    list.Remove(arr[i]);
                    if (check)
                    {
                        return;
                    }
                }
            }
        }
        static void Main(string[] args)
        {
            arr = new int[9];
            for (int i = 0; i < 9; i++)
            {
                arr[i] = int.Parse(Console.ReadLine());
            }
            dfs(0, 0, 0);
            Console.WriteLine(sb.ToString());
        }
    }
}
