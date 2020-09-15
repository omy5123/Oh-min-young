using System;

using System.Collections.Generic;
using System.Text;

namespace _1927__최소_힙_
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            List<int> list = new List<int>();
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++)
            {
                int a = int.Parse(Console.ReadLine());
                if (a == 0)
                {
                    if (list.Count ==0)
                    {
                        sb.AppendLine("0");
                    }
                    else
                    {
                        list.Sort();
                        sb.AppendLine(list[0]+"");
                        list.Remove(list[0]);
                    }
                    
                }
                else
                {
                    list.Add(a);
                }
                
            }
            Console.WriteLine(sb.ToString());
            
        }
    }
}
