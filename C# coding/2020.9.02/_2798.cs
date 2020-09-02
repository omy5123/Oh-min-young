using System;

namespace _2798__브루트포스_
{
    class _2798
    {
        static int n = 0;
        static int m = 0;
        static int sum = 0;
        static bool[] check = { };
        static int[] arr = { };
        static int s = 0;
        static void dfs(int cnt, int sum)
        {
            if (cnt == 3)
            {
                if (sum <= m)
                {
                    if ((m - s) > (m - sum))
                    {
                        s = sum;
                    }
                    return;
                }
                
            }
            else
            {
                for (int i = 0; i < n; i++)
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

        }
        static void Main(string[] args)
        {
            string[] nm = Console.ReadLine().Split();
            n = int.Parse(nm[0]);
            m = int.Parse(nm[1]);
            arr = new int[n];
            check = new bool[n];
            string[] ar = Console.ReadLine().Split();
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(ar[i]);
            }
            dfs(0,sum);
            Console.WriteLine(s);
        }
    }
}
