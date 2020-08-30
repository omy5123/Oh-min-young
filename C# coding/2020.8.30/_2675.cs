using System;
using System.Text;

namespace _2675
{
    class Program
    {
        static void Main(string[] args)
        {
            int t = int.Parse(Console.ReadLine());
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < t; i++)
            {
                string[] ar = Console.ReadLine().Split();
                int a = int.Parse(ar[0]);
                string arr = ar[1];

                for (int j = 0; j < arr.Length; j++)
                {
                    result.Append(arr[j], a);
                }
                result.AppendLine();
            }
            Console.WriteLine(result);

        }
    }
}
