using System;

namespace _1149__RGB거리_
{
    class _1149
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());

            int[,] arr = new int[n, 3];
            for (int i = 0; i < n; i++)
            {
                string[] line = Console.ReadLine().Split();
                for (int j = 0; j < 3; j++)
                {
                    arr[i, j] = int.Parse(line[j]);
                }
            }
            for (int i = 1; i < n; i++)
            {
                arr[i, 0] += Math.Min(arr[i - 1, 1], arr[i - 1, 2]);
                arr[i, 1] += Math.Min(arr[i - 1, 0], arr[i - 1, 2]);
                arr[i, 2] += Math.Min(arr[i - 1, 0], arr[i - 1, 1]);
            }
            int min = int.MaxValue;
            for (int i = 0; i < 3; i++)
            {
                if(min > arr[n-1,i])
                {
                    min = arr[n - 1, i];
                }
            }
            Console.WriteLine(min);
        }
    }
}
