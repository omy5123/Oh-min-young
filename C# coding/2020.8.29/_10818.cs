using System;

namespace C_sharp_study
{
    class _10818
    {
        static int Min(int x, int y)
        {
            if (x<y)
            {
                return x;
            }
            else
            {
                return y;
            }
        }
        static int Max(int x, int y)
        {
            if (x < y)
            {
                return y;
            }
            else
            {
                return x;
            }

        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string[] ar = Console.ReadLine().Split();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(ar[i]); 
            }
            int min = arr[0], max = arr[0];
            for (int i = 1; i < n; i++)
            {
                min = Min(min, arr[i]);
                max = Max(max, arr[i]);
            }
            Console.WriteLine($"{min} {max}");
        }
    }
}
