using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

namespace _5639__이진_검색_트리_
{
    class _5639
    {
        static List<int> list = new List<int>();
        static void Main(string[] args)
        {
            while (true)
            {
                try
                {
                    int temp = int.Parse(Console.ReadLine());
                    list.Add(temp);
                }
                catch (Exception e) { break; }
            }
            MakeBFS(0, list.Count - 1);
        }

        static void MakeBFS(int left, int right)
        {
            if (left > right)
                return;

            int root = list[left];
            int last = right;

            while (list[last] > root)
                last--;

            MakeBFS(left + 1, last);
            MakeBFS(last + 1, right);
            Console.WriteLine(root);
        }
    }
}
