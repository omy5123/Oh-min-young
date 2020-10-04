using System;

namespace _1051__숫자_정사각형_
{
    class _1051
    {
        static void Main(string[] args)
        {
            string[] nm = Console.ReadLine().Split();
            int n = int.Parse(nm[0]);
            int m = int.Parse(nm[1]);
            int[,] arr = new int[n, m];
            for (int i = 0; i < n; i++)
            {
                string line = Console.ReadLine();
                for (int j = 0; j < m; j++)
                {
                    arr[i, j] = int.Parse(line[j].ToString());
                }
            }
            int min = Math.Min(n, m);
            int max = 0;
            
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    for (int k = 1; k < min; k++)
                    {
                        if (i + k < n && j + k < m)
                        {
                            if (arr[i, j] == arr[i, j + k] && arr[i, j] == arr[i + k, j] && arr[i, j] == arr[i + k, j + k])
                            {
                                if (max < k)
                                {
                                    max = k;
                                }
                            }
                        }
                    }
                }
            }
            
            Console.WriteLine((max + 1) * (max + 1));
        }
    }
}
