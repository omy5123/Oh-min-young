using System;
using System.Linq;

namespace _2458__키_순서_
{
    class _2458
    {
        static int[,] arr;
        static int n;
        static int m;
        
        static void Main(string[] args)
        {
            string[] nm = Console.ReadLine().Split();
            n = int.Parse(nm[0]);
            m = int.Parse(nm[1]);
            arr = new int[n + 1, n + 1];
            
            for (int i = 0; i < m; i++)
            {
                string[] ab = Console.ReadLine().Split();
                int a = int.Parse(ab[0]);
                int b = int.Parse(ab[1]);
                arr[a, b] = 1;
            }
            for (int k = 1; k < n+1; k++)
            {
                for (int i = 1; i < n+1; i++)
                {
                    for (int j = 1; j < n+1; j++)
                    {
                        if(arr[i,k] + arr[k,j] == 2)
                        {
                            arr[i, j] = 1;
                        }
                    }
                }
            }
            int[] cnt = new int[n + 1];
            for (int i = 1; i < n+1; i++)
            {
                for (int j = 1; j < n+1; j++)
                {
                    if (arr[i,j] == 1)
                    {
                        cnt[i] += 1;
                        cnt[j] += 1;
                    }
                }
            }
            int count = 0;
            for (int i = 1; i < n+1; i++)
            {
                if(cnt[i] == n-1)
                {
                    count += 1;
                }
            }
            Console.WriteLine(count);
        }
    }
}
