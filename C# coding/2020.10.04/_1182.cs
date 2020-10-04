using System;

namespace _1182__부분수열의_합_
{
    class _1182
    {
        static int count;
        static int n;
        static int s;
        static int[] arr;

        static void dfs(int cnt, int i, int idx, int sum)
        {
            if (cnt == i)
            {
                if (sum == s)
                {
                    count += 1;
                    return;
                }
            }
            else
            {
                for (int j = idx; j < n; j++)
                {
                    dfs(cnt + 1, i, j + 1, sum + arr[j]);
                }
            }

        }
        static void Main(string[] args)
        {
            string[] st = Console.ReadLine().Split();
            n = int.Parse(st[0]);
            s = int.Parse(st[1]);

            string[] line = Console.ReadLine().Split();
            arr = new int[n];
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(line[i]);
            }

            for (int i = 1; i < n + 1; i++)
            {
                dfs(0, i, 0, 0);
            }
            Console.WriteLine(count);
        }
    }
}
