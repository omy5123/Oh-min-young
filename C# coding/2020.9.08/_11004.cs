using System;

namespace _11004__k번째_수_
{
    class _11004
    {
        static void Main(string[] args)
        {
            string[] nk = Console.ReadLine().Split();
            int n = int.Parse(nk[0]);
            int k = int.Parse(nk[1]);

            string[] ar = Console.ReadLine().Split();
            int[] arr = new int[ar.Length];
            for (int i = 0; i < ar.Length; i++)
            {
                arr[i] = Convert.ToInt32(ar[i]);
            }
            Array.Sort(arr);
            Console.WriteLine(arr[k - 1]);
        }
    }
}
