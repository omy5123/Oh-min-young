using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace _11728__배열_합치기_
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] nm = Console.ReadLine().Split();
            int n = int.Parse(nm[0]);
            int m = int.Parse(nm[1]);
            List<int> list = new List<int>();
            StringBuilder sb = new StringBuilder();
            string[] a = Console.ReadLine().Split();
            foreach (var item in a)
            {
                list.Add(int.Parse(item));
            }
            string[] b = Console.ReadLine().Split();
            foreach (var item in b)
            {
                list.Add(int.Parse(item));
            }
            list.Sort();
            foreach (var item in list)
            {
                sb.Append(item + " ");
            }
            Console.WriteLine(sb);

        }
    }
}
