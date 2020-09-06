using System;
using System.Collections.Generic;

namespace _1427__sort_
{
    class _1427
    {
        static void Main(string[] args)
        {
            string str = Console.ReadLine();
            List<char> arr = new List<char>();
            for (int i = 0; i < str.Length; i++)
            {
                arr.Add(str[i]);
            }
            arr.Sort();
            arr.Reverse();
            Console.WriteLine(string.Join("", arr));
        }
    }
}
