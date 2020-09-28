using System;

namespace _10808__알파벳_개수_
{
    class _10808
    {
        static void Main(string[] args)
        {
            string str = Console.ReadLine();
            int[] alpha = new int[26];
            
            foreach (int i in str)
            {
                alpha[(int)i-97] += 1;
            }
            Console.WriteLine(string.Join(" ", alpha));
        }
    }
}
