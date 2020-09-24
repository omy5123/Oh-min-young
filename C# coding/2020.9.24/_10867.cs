using System;
using System.Linq;

namespace _10867__중복_빼고_정렬하기_
{
    class _10867
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int[] arr = new int[n];
            string[] str = Console.ReadLine().Split();
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(str[i]);
            }
            arr = arr.Distinct().ToArray();
            Array.Sort(arr);
            Console.WriteLine(string.Join(" ", arr));
        }
    }
}
