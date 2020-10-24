using System;

namespace _6996__애너그램_
{
    class _6996
    {
        static void solution(int n, string[,] arr)
        {
            for (int i = 0; i < n; i++)
            {
                string a = arr[i, 0];
                string b = arr[i, 1];
                char[] a_arr = a.ToCharArray();
                char[] b_arr = b.ToCharArray();
                Array.Sort(a_arr);
                Array.Sort(b_arr);
                
                if ((string.Join("",a_arr) == string.Join("", b_arr)))
                {
                    Console.WriteLine($"{a} & {b} are anagrams.");
                }
                else
                {
                    Console.WriteLine($"{a} & {b} are NOT anagrams.");
                }
            }
        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string[,] arr = new string[n, 2];
            for (int i = 0; i < n; i++)
            {
                string[] line = Console.ReadLine().Split();
                arr[i, 0] = line[0];
                arr[i, 1] = line[1];
            }
            solution(n, arr);
        }
    }
}
