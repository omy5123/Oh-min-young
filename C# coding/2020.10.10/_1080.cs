using System;

namespace _1080__행렬_
{
    class _1080
    {
        static int cnt = 0;
        static int solve(int n, int m, int[,] arr, int[,] brr, bool[,] s)
        {
            for (int i = 0; i < n - 2; i++)
            {
                for (int j = 0; j < m - 2; j++)
                {
                    if (s[i, j] == false)
                    {
                        for (int k = i; k < i+3; k++)
                        {
                            for (int l = j; l < j+3; l++)
                            {
                                s[k, l] = !(s[k, l]);
                            }
                        }
                    }
                    cnt += 1;
                }
            }
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    if (s[i, j] == false)
                    {
                        return -1;
                    }
                }
            }
            return cnt;
        }
        static void Main(string[] args)
        {
            string[] nm = Console.ReadLine().Split();
            int n = int.Parse(nm[0]);
            int m = int.Parse(nm[1]);
            int[,] arr = new int[n, m];
            int[,] brr = new int[n, m];

            for (int i = 0; i < n; i++)
            {
                string line = Console.ReadLine();
                for (int j = 0; j < m; j++)
                {
                    arr[i, j] = int.Parse(line[j].ToString());
                }
            }
            for (int i = 0; i < n; i++)
            {
                string line = Console.ReadLine();
                for (int j = 0; j < m; j++)
                {
                    brr[i, j] = int.Parse(line[j].ToString());
                }
            }
            bool[,] s = new bool[n, m];
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    if (arr[i, j] == brr[i, j])
                    {
                        s[i, j] = true;
                    }
                    else
                    {
                        s[i, j] = false;
                    }
                }
            }
            if (n >= 3 && m >= 3)
            {
                Console.WriteLine(solve(n, m, arr, brr, s));
            }
            else
            {
                bool check = true;
                for (int i = 0; i < n; i++)
                {
                    for (int j = 0; j < m; j++)
                    {
                        if(s[i,j] == false)
                        {
                            check = false;
                            break;
                        }
           
                    }
                    if(check == false)
                    {
                        break;
                    }
                }
                if (check)
                {
                    Console.WriteLine(0);
                }
                else
                {
                    Console.WriteLine(-1);
                }
                
            }
        }
    }
}
