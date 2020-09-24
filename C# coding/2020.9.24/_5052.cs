using System;
using System.Text;

namespace _5052__전화번호_목록_
{
    class _5052
    {
        static int n = 0;
        static void Main(string[] args)
        {
            int t = int.Parse(Console.ReadLine());
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < t; i++)
            {
                n = int.Parse(Console.ReadLine());
                string[] arr = new string[n];
                for (int j = 0; j < n; j++)
                {
                    arr[j] = Console.ReadLine();
                }
                Array.Sort(arr);
                bool check = true;
                for (int k = 0; k < n-1; k++)
                {
                    if (arr[k+1].Contains(arr[k]))
                    {
                        check = false;
                        break;
                    }
                }
                if (check)
                {
                    sb.AppendLine("YES");
                }
                else
                {
                    sb.AppendLine("NO");
                }
            }
            Console.WriteLine(sb);
        }
    }
}
