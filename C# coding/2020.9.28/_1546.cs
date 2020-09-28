using System;
using System.Linq;

namespace _1546
{
    class _1546
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string[] str = Console.ReadLine().Split();
            int[] arr = new int[n];
            for(int i=0;i<n;i++)
            {
                arr[i] = int.Parse(str[i]);
            }
            float s = arr.Sum()/n;
            Console.WriteLine(s);
        }
    }
}
