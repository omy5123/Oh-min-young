using System;

namespace _1976__여행_가자_
{
    class _1976
    {
        static bool flag;
        static void dfs(int start, int end, int n, int m, int[,] arr,bool[] visit)
        {
            if (start == end)
            {
                flag = true;
                return;
            }
            else
            {
                for (int i = 0; i < n; i++)
                {
                    if (flag == false && arr[start - 1, i] == 1&& visit[i] == false)
                    {
                        visit[i] = true;
                        dfs(i + 1, end, n, m, arr,visit);
                        if (flag == true)
                        {
                            return;
                        }
                    }
                }
            }
        }
        static void solution(int n, int m, int[,] arr, int[] check)
        {
            bool[] visit = new bool[n];

            for (int i = 0; i < m - 1; i++)
            {
                int start = check[i];
                int end = check[i + 1];
                flag = false;
                dfs(start, end, n, m, arr,visit);
                if (flag == false)
                {
                    Console.WriteLine("NO");
                    return;
                }
            }
            Console.WriteLine("YES");
        }


        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int m = int.Parse(Console.ReadLine());
            int[,] arr = new int[n, n];
            for (int i = 0; i<n;i++)
            {
                string[] line = Console.ReadLine().Split();
                for(int j=0;j<n;j++)
                {
                    arr[i, j] = int.Parse(line[j]);
                }
            }
            
            int[] check = new int[m];
            string[] st = Console.ReadLine().Split();
            for(int i =0; i<m;i++)
            {
                check[i] = int.Parse(st[i]);
            }
            solution(n, m, arr, check);
        }
    }
}
