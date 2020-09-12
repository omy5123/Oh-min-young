using System;
using System.Collections.Generic;

namespace _1463
{
    class _1463
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            List<int> dp = new List<int>() { 0,0,1,1,2,3 };
            for (int i = 6; i < n+1; i++)
            {
                if (i % 3 == 0)
                {
                    int a = dp[i / 3];
                    int c = dp[i - 1];
                    int min = Math.Min(a, c);
                    if (i % 2 == 0)
                    {
                        int b = dp[i / 2];
                        dp.Add(Math.Min(min, b)+1);
                    }
                    else
                    {
                        dp.Add(min+1);
                    }
                }
                else if (i % 2 == 0)
                {
                    int min = (Math.Min(dp[i / 2], dp[i - 1]))+1;
                    dp.Add(min);
                }
                else
                {
                    dp.Add(dp[i - 1]+1);
                }
            }
            
            Console.WriteLine(dp[n]);
            
        }
    }
}
