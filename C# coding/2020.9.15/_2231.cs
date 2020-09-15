using System;

namespace _2231__분해합_
{
    class _2231
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());

            for (int i = 1; i < n; i++)
            {
                int sum = i;
                int a = i;
                while (a > 0)
                {
                    sum += a % 10;
                    a = a / 10;
                }
                if (sum == n)
                {
                    Console.WriteLine(i);
                    return;
                }
            }
            Console.WriteLine(0);
        }
    }
}
