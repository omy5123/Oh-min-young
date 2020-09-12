using System;

namespace _1912__연속합_
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string[] st = Console.ReadLine().Split();
            int[] arr = new int[n+1];
            arr[0] = 0;
            for (int i = 1; i < n+1; i++)
            {
                arr[i] = int.Parse(st[i-1]);
            }
            int sum = Int32.MinValue;
            int[] dp = new int[n + 1];
            
            for (int i = 1; i < n+1; i++)
            {
                dp[i] = Math.Max(arr[i], dp[i - 1] + arr[i]);
                sum = Math.Max(sum, dp[i]);
            }
            Console.WriteLine(sum);
        }
    }
}
