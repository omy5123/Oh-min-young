using System;
using System.Runtime.CompilerServices;

namespace _9663__N_Queen_
{
    class _9663
    {
        static int n = 0;
        static int[] col;
        static int[] d1;
        static int[] d2;
        static int result = 0;
        static bool Adjacent(int x)
        {
            for (int i = 0; i < x; i++)
            {
                if (col[x] == col[i] || Math.Abs(col[x]-col[i]) == x-i) 
                {
                    return false;
                }
            }
            return true;
        }
        static void dfs(int cnt)
        {
            if (cnt == n)
            {
                result += 1;
                return;
            }
            for (int i = 0; i < n; i++)
            {
                col[cnt] = i;
                if (Adjacent(cnt))
                {
                    dfs(cnt + 1);
                }
            }
        }
        static void Main(string[] args)
        {
            n = int.Parse(Console.ReadLine());
            col = new int[n];
            dfs(0);
            Console.WriteLine(result);
        }
        
    }
}
