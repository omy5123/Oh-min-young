using System;

namespace _10819__차이를_최대로_
{
    class _10819
    {
        static int max = int.MinValue;
        static void dfs(int cnt, int[] arr, bool[] check, int n, int[] brr)
        {
            if (cnt == n)
            {
                int sum = 0;
                for (int i = 0; i < n - 1; i++)
                {
                    sum += Math.Abs(brr[i] - brr[i + 1]);
                }
                if (max < sum)
                {
                    max = sum;
                }
            }
            else
            {
                for (int i = 0; i < n; i++)
                {
                    if (check[i] == true)
                    {
                        continue;
                    }
                    else
                    {
                        check[i] = true;
                        brr[cnt] = arr[i];
                        dfs(cnt + 1, arr, check, n,brr);
                        brr[cnt] = 0;
                        check[i] = false;
                    }
                }
            }
        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string[] st = Console.ReadLine().Split();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(st[i]);
            }
            bool[] check = new bool[n];
            int[] brr = new int[n];
            dfs(0, arr, check, n, brr);
            Console.WriteLine(max);
        }
    }
}
