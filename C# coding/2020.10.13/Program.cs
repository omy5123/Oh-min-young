using System;

namespace _2752__세수정렬_
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] str = Console.ReadLine().Split();
            int[] num = new int[3];
            for (int i = 0; i < 3; i++)
            {
                num[i] = int.Parse(str[i]);
            }
            Array.Sort(num);
            Console.WriteLine(string.Join(" ", num));
        }
    }
}
