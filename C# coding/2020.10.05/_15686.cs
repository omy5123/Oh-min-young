using System;
using System.Collections.Generic;
using System.Linq;

namespace _15686__치킨_배달_
{
    class _15686
    {
        static int n;
        static int m;
        static int[,] arr;
        static Stack<(int, int)> stack = new Stack<(int, int)>();
        static int result = int.MaxValue;
        static void dfs(int cnt, int idx, List<(int, int)> list)
        {
            if (cnt == m)
            {
                int min = 0;
                for (int i = 0; i < n; i++)
                {
                    for (int j = 0; j < n; j++)
                    {
                        if (arr[i, j] == 1)
                        {
                            int sum = int.MaxValue;
                            List<(int, int)> li = stack.ToList();
                            for (int k = 0; k < li.Count; k++)
                            {
                                int len = Math.Abs(li[k].Item1 - i) + Math.Abs(li[k].Item2 - j);
                                if (sum > len)
                                {
                                    sum = len;
                                }
                            }
                            min += sum;
                        }
                    }
                }
                if (result > min)
                {
                    result = min;
                }
            }
            else
            {
                for (int i = idx; i < list.Count; i++)
                {
                    stack.Push((list[i].Item1, list[i].Item2));
                    dfs(cnt + 1, i + 1, list);
                    stack.Pop();
                }
            }
        }
        static void Main(string[] args)
        {
            string[] nm = Console.ReadLine().Split();
            n = int.Parse(nm[0]);
            m = int.Parse(nm[1]);
            arr = new int[n, n];
            for (int i = 0; i < n; i++)
            {
                string[] line = Console.ReadLine().Split();
                for (int j = 0; j < n; j++)
                {
                    arr[i, j] = int.Parse(line[j].ToString());
                }
            }
            List<(int, int)> list = new List<(int, int)>();
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (arr[i, j] == 2)
                    {
                        list.Add((i, j));
                    }
                }
            }
            dfs(0, 0, list);
            Console.WriteLine(result);
        }
    }
}
