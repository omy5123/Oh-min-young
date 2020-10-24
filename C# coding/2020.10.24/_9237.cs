using System;
using System.Linq;

namespace _9237__이장님_초대_
{
    class Program
    {
        static void solution(int n, int[] arr)
        {
            Array.Sort(arr);
            Array.Reverse(arr);
            int sum = 0;
            for (int i = 1; i < n+1; i++)
            {
                sum = Math.Max(sum, arr[i-1] + i);
            }
            Console.WriteLine(sum + 1);
        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int[] arr = new int[n];
            string[] line = Console.ReadLine().Split();
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(line[i]);
            }
            solution(n, arr);
        }
    }
}
