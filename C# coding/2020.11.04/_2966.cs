using System;
using System.Linq;

namespace _2966__찍기_
{
    class _2966
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());

            string str = Console.ReadLine();

            int a = 0;
            int b = 0;
            int c = 0;
            for (int i = 0; i < str.Length; i++)
            {
                if(i % 3 == 0)
                {
                    if(str[i] == 'A')
                    {
                        a += 1;
                    }
                }
                else if (i % 3 == 1)
                {
                    if(str[i] == 'B')
                    {
                        a += 1;
                    }
                }
                else
                {
                    if(str[i] == 'C')
                    {
                        a += 1;
                    }
                }

                if (i % 4 == 0 || i % 4 == 2)
                {
                    if (str[i] == 'B')
                    {
                        b += 1;
                    }
                }
                else if (i % 4 == 1)
                {
                    if (str[i] == 'A')
                    {
                        b += 1;
                    }
                }
                else
                {
                    if (str[i] == 'C')
                    {
                        b += 1;
                    }
                }

                if (i % 6 == 0 || i% 6 ==1)
                {
                    if (str[i] == 'C')
                    {
                        c += 1;
                    }
                }
                else if (i % 6 == 2 || i% 6 == 3)
                {
                    if (str[i] == 'A')
                    {
                        c += 1;
                    }
                }
                else
                {
                    if (str[i] == 'B')
                    {
                        c += 1;
                    }
                }
            }
            int[] max = { a, b, c };
            int m = max.Max();
            Console.WriteLine(m);

            if(a == m)
            {
                Console.WriteLine("Adrian");
            }
            if(b == m)
            {
                Console.WriteLine("Bruno");
            }
            if (c == m)
            {
                Console.WriteLine("Goran");
            }
        }
    }
}
