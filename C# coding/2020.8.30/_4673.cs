using System;
using System.Text;

namespace _4673
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] arr = new int[10001];
            for (int i = 1; i < 10001; i++)
            {
                int a = i / 1000;
                int b = i / 100 % 10;
                int c = i / 10 % 10;
                int d = i % 10;
                int s = a + b + c + d + i;
                if (s > 10000)
                {
                    continue;
                }
                arr[s] = s;
            }
            for (int i = 1; i < 10001; i++)
            {
                if (arr[i] == 0)
                {
                    Console.WriteLine(i);
                }
            }
        }
    }
}
