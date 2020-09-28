using System;

namespace _11721__열_개씩_끊어_출력하기_
{
    class _11721
    {
        static void Main(string[] args)
        {
            string str = Console.ReadLine();
            
            for(int i = 0;i<str.Length;i++)
            {
                if(i == 0)
                {
                    Console.Write(str[i]);
                    continue;
                }
                if (i % 10 == 0)
                    Console.WriteLine();
                Console.Write(str[i]);
            }
        }
    }
}
