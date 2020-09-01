using System;
using System.Text;


namespace _15649__백트래킹_
{
    class _15649
    {
        static int n, m;
        static StringBuilder result = new StringBuilder();
        static bool[] check = new bool[8];
        static int [] arr = new int[8];
        static void dfs(int cnt)
        {
            if (cnt==m)
            {
                for (int i = 0; i < m; i++)
                {
                    result.Append(arr[i]);
                    result.Append(" ");
                }
                result.Append("\n");
            }
            else
            {
                for (int i = 0; i < n; i++)
                {
                    if (!check[i])
                    {
                        check[i] = true;
                        arr[cnt] = i + 1;
                        dfs(cnt + 1);
                        check[i] = false;
                    }
                }
            }
        }
        static void Main(string[] args)
        {
            string[] a = Console.ReadLine().Split();
            n = int.Parse(a[0]);
            m = int.Parse(a[1]);
            dfs(0);
            Console.WriteLine(result.ToString());
        }

    }
}