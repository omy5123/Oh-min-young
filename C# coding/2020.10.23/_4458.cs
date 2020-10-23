using System;
using System.Text;

namespace _4458
{
    class _4458
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++)
            {
                string str = Console.ReadLine();
                if (97 <= str[0] && str[0] < 123)
                {
                    sb.Append((char)(str[0] - 32));
                }
                else
                {
                    sb.Append(str[0]);
                }
                sb.AppendLine(str.Substring(1));
                
            }
            Console.WriteLine(sb);
        }
    }
}
