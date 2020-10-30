using System;
using System.Reflection.Metadata;

namespace _2960__에라토스테네스의_체_
{
    class _2960
    {
        static void Main(string[] args)
        {
            string[] nk = Console.ReadLine().Split();
            int n = int.Parse(nk[0]);
            int k = int.Parse(nk[1]);

            bool[] check = new bool[n + 1];
            int cnt = 0;

            for (int i = 2; i < n+1; i++)
            {
                for (int j = i; j < n+1;)
                {
                    if(check[j]==false)
                    {
                        check[j] = true;
                        cnt += 1;
                        if(cnt == k)
                        {
                            Console.WriteLine(j);
                            return;
                        }
                    }
                    j = j + i;
                }
            }
        }
    }
}
