using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace _1764__듣보잡_
{
    class _1764
    {
        static void Main(string[] args)
        {
            SortedSet<string> p = new SortedSet<string>();
            SortedSet<string> r = new SortedSet<string>();
            StringBuilder sb = new StringBuilder();
            string[] ar = Console.ReadLine().Split();
            int n = int.Parse(ar[0]);
            int m = int.Parse(ar[1]);
            
            for (int i = 0; i < n; i++)
            {
                p.Add(Console.ReadLine());
            }

            for (int i = 0; i < m; i++)
            {
                string s = Console.ReadLine();
                if (p.Contains(s))
                {
                    r.Add(s);
                }
            }
            sb.Append(r.Count);
            sb.AppendLine();
            foreach (var item in r)
            {
                sb.AppendLine(item);
            }
            Console.WriteLine(sb);
            foreach (var item in r)
            {
                Console.WriteLine(item);
            }
            
            /*string[] ar = Console.ReadLine().Split();
            StringBuilder sb = new StringBuilder();
            int n = int.Parse(ar[0]);
            int m = int.Parse(ar[1]);
            string[] str = new string[n];
            for (int i = 0; i < n; i++)
            {
                str[i] = Console.ReadLine();
            }
            List<string> list = new List<string>();
            for (int i = 0; i < m; i++)
            {
                string s = Console.ReadLine();
                if (str.Contains(s) == true)
                {
                    list.Add(s);
                }
            }
            list.Sort();
            sb.Append(list.Count);
            sb.AppendLine();
      
            foreach (var item in list)
            {
                sb.AppendLine(item);
            }
            Console.WriteLine(sb);
            */
        }
    }
}
