using System;
using System.Text;

namespace _11944__NN_
{
    class _11944
    {
        static void Main(string[] args)
        {
            StringBuilder sb = new StringBuilder();
            string[] nm = Console.ReadLine().Split();
            int n = int.Parse(nm[0]);
            int m = int.Parse(nm[1]);

            for (int i = 0; i < n; i++)
            {
                sb.Append(n);
            }
            
            if(sb.Length > m)
            {
                string s = sb.ToString().Substring(0,m);
                Console.WriteLine(s);
            }
            else
            {
                Console.WriteLine(sb);
            }
            
        }
    }
}
