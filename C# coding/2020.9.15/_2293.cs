using System;

namespace _2293__동전1_
{
    class _2293
    {
        static void Main(string[] args)
        {
            string[] nk = Console.ReadLine().Split();
            int n = int.Parse(nk[0]);
            int k = int.Parse(nk[1]);

            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(Console.ReadLine());
            }
            int[] dp = new int[k+1];
            dp[0] = 1;
            foreach (int i in arr)
            {
                for (int j = 1; j < k + 1; j++)
                {
                    if (j - i >= 0)
                    {
                        dp[j] = dp[j - i] + dp[j];
                    }
                }
            }
            Console.WriteLine(dp[k]);
            
        }
    }
}
