using System;
using System.Collections.Generic;

namespace _1371__가장_많은_글자_
{
    class Program
    {
        static List<string> list = new List<string>();
        static void Main(string[] args)
        {
            while (true)
            {
                try
                {
                    string temp = Console.ReadLine();
                    list.Add(temp);
                }
                catch (Exception e) { break;}
            }
            Console.WriteLine(list[0]);
        }
    }
}
