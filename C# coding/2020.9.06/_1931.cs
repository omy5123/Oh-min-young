using System;
using System.Collections.Generic;

namespace _1931__sort_회의실배정_
{
    class _1931
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            List<(int,int)> arr = new List<(int,int)>();
            for (int i = 0; i < n; i++)
            {
                string[] st = Console.ReadLine().Split();
                int a = int.Parse(st[0]);
                int b = int.Parse(st[1]);
                arr.Add((a, b));
            }
            
        }
    }
}
