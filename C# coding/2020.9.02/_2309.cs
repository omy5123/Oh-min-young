using System;
using System.Collections.Generic;

namespace _2309__브루트포스_
{
    class _2309
    {
        static int sum = 0;
        static int[] arr = new int[9];
        static List<int> brr = new List<int>();
        static bool[] check = new bool[9];
        static bool result = false;
        static void dfs(int cnt,int sum)
        {
            if (result)
            {
                return;
            }
            if (cnt == 7)
            {
                if (sum == 100)
                {
                    for (int i = 0; i < 9; i++)
                    {
                        if (check[i])
                        {
                            brr.Add(arr[i]);
                        }
                    }
                    result = true;
                }
            }
            for (int i = 0; i < 9; i++)
            {
                if (check[i])
                {
                    continue;
                }
                check[i] = true;
                dfs(cnt + 1, sum + arr[i]);
                check[i] = false;
            }
            
        }
        static void Main(string[] args)
        {
            for (int i = 0; i < 9; i++)
            {
                arr[i] = int.Parse(Console.ReadLine());
            }
            dfs(0,sum);
            brr.Sort();
            foreach (var br in brr)
            {
                Console.WriteLine(br);
            }
        }
    }
}
