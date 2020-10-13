using System;
using System.Text;

namespace _11365
{
    class _11365
    {
        static void Main(string[] args)
        {
            StringBuilder sb = new StringBuilder();
            while (true)
            {
                string str = Console.ReadLine();
                if(str == "END")
                {
                    break;
                }
                else
                {
                    char[] arr = str.ToCharArray();
                    Array.Reverse(arr);
                    sb.AppendLine(string.Join("", arr));
                }
            }
            Console.WriteLine(sb);
        }
    }
}
