using System;
using System.Linq;

namespace _11053__가장_긴_증가하는_부분수열_
{
    class _11053
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string[] st = Console.ReadLine().Split();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(st[i]);
            }
            int[] dp = new int[n];
            for (int i = 0; i < n; i++)
            {
                dp[i] = 1;
                for (int j = 0; j < i; j++)
                {
                    if (arr[j]<arr[i]&&dp[j]+1>dp[i])
                    {
                        dp[i] += 1;
                    }
                }
            }
            Console.WriteLine(dp.Max());
        }
    }
}
