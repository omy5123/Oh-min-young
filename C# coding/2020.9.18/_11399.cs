using System;

namespace _11399__ATM_
{
    class _11399
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string[] ar = Console.ReadLine().Split();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(ar[i]);
            }
            Array.Sort(arr);
            int sum = arr[0];
            for (int i = 1; i < n; i++)
            {
                arr[i] = arr[i]+arr[i - 1];
                sum += arr[i];
            }
            Console.WriteLine(sum);
        }
    }
}
