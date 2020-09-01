using System;
using System.Collections.Generic;

namespace _2309__브루트포스_
{
    class _2309
    {
        static int sum = 0;
        static int[] arr = new int[9];
        static List<int> brr = new List<int>();
        static bool[] check = new bool[9];
        static void dfs(int k,int cnt)
        {
            if (sum > 100)
            {
                return;
            }
            else
            {
                for (int i = k; i < 9; i++)
                {
                    if (!(check[i]))
                    {
                        check[i] = true;
                        brr.Add(arr[cnt]);
                        sum += arr[cnt];
                        if (sum == 100)
                        {
                            return;
                        }
                        dfs(i+1,cnt + 1);
                        brr.Remove(arr[cnt]);
                        sum -= arr[cnt];
                        check[i] = false;
                    }
                }
                
            }
           
        }
        static void Main(string[] args)
        {
            for (int i = 0; i < 9; i++)
            {
                arr[i] = int.Parse(Console.ReadLine());
            }
            dfs(0,0);
            brr.Sort();
            foreach (var br in brr)
            {
                Console.WriteLine(br);
            }
        }
    }
}
