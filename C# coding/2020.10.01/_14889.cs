using System;
using System.Collections.Generic;

namespace _14889__스타트와_링크_
{
    class Program
    {
        static int n;
        static int[,] arr;
        static bool[] check;
        static List<int> index_2 = new List<int>();

        static int result = int.MaxValue;
        static void dfi(int i, int j , List<int> index_1,int cnt,int idx)
        {
            
            if (cnt == n/2)
            {
                int sum = 0;
                Console.WriteLine($"{i} {j}");
                Console.WriteLine($"{index_2[0]} {index_2[1]}");
                sum = Math.Abs(arr[i,j] + arr[j,i] - (arr[index_2[0],index_2[1]] + arr[index_2[1], index_2[0]]));
                Console.WriteLine(sum);
                if (sum < result)
                {
                    result = sum;
                }
            }
            else
            {
                for (int k = idx; k < index_1.Count; k++)
                { 
                    index_2.Add(index_1[k]);
                    dfi(i, j, index_1, cnt + 1,k + 1);
                    index_2.Remove(index_1[k]);
                }
            }
        }
        static void check_dfs(int i, int j)
        {
            List<int> index_1 = new List<int>();
            for (int k = 0; k < n; k++)
            {
                if (k == i|| k==j)
                {
                    continue;
                }
                else
                {
                    index_1.Add(k);
                }
            }
            dfi(i, j, index_1,0,0);
        }
        static void dfs(int cnt,int idx)
        {
            if (cnt == n/2)
            {
                List<int> index = new List<int>();
                for (int j = 0; j < n; j++)
                {
                    if (check[j] == true)
                    {
                        index.Add(j);
                    }
                }
                
                check_dfs(index[0], index[1]);
            }
            else
            {
                for (int i = idx; i < n; i++)
                {
                    check[i] = true;
                    dfs(cnt + 1,i+1);
                    check[i] = false;
                    
                }
            }
        }
        static void Main(string[] args)
        {
            n = int.Parse(Console.ReadLine());
            arr = new int[n, n];
            check = new bool[n];
            for (int i = 0; i < n; i++)
            {
                string[] line = Console.ReadLine().Split();
                for (int j = 0; j < n; j++)
                {
                    arr[i, j] = int.Parse(line[j].ToString());
                }
            }
            dfs(0,0);
            Console.WriteLine(result);
        }
    }
}
