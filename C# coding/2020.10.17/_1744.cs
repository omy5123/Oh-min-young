using System;
using System.Collections.Generic;
namespace _1744__수묶기_
{
    class _1744
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            List<int> ne = new List<int>();
            List<int> po = new List<int>();
            int answer = 0;
            for (int i = 0; i < n; i++)
            {
                int num = int.Parse(Console.ReadLine());
                if (num <= 0)
                {
                    ne.Add(num);
                }
                else if (num == 1)
                {
                    answer += 1;
                }
                else
                {
                    po.Add(num);
                }
            }
            ne.Sort();
            po.Sort();
            po.Reverse();
            for (int i = 0; i < ne.Count; i = i + 2)
            {
                if (i + 1 < ne.Count)
                {
                    answer += ne[i] * ne[i + 1];
                }
                else
                {
                    answer += ne[i];
                }
            }
            for (int i = 0; i < po.Count; i = i + 2)
            {
                if (i + 1 < po.Count)
                {
                    answer += po[i] * po[i + 1];
                }
                else
                {
                    answer += po[i];
                }
            }
            Console.WriteLine(answer);
        }
    }
}
