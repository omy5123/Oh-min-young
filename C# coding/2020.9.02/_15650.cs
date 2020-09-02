using System;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Text;

namespace _15650__백트래킹_
{
    class _15650
    {
        static int n, m;
        static StringBuilder result = new StringBuilder();
        static bool[] check = new bool[8];
        static int[] arr = new int[8];
        static void dfs(int k,int cnt)
        {
            if (cnt == m)
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
                for (int i = k; i < n; i++)
                {
                    if (!check[i])
                    {
                        arr[cnt] = i + 1;
                        dfs(i,cnt + 1);
                    }
                }
            }
        }
        static void Main(string[] args)
        {
            string[] a = Console.ReadLine().Split();
            n = int.Parse(a[0]);
            m = int.Parse(a[1]);
            dfs(0,0);
            Console.WriteLine(result.ToString());
        }

    }
}
