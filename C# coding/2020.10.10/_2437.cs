using System;
using System.Text;

namespace _2437__저울_
{
    class _2437
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string[] str_arr = Console.ReadLine().Split();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(str_arr[i]);
            }
            Array.Sort(arr);
            int num = 1;
            for (int i = 0; i < n; i++)
            {
                if (num < arr[i])
                {
                    break;
                }
                num += arr[i];
            }
            Console.WriteLine(num);
        }
    }
}
