using System;
using System.Collections.Generic;
using System.ComponentModel.Design;

namespace _1094
{
    class _1094
    {
        static void Main(string[] args)
        {
            int x = int.Parse(Console.ReadLine());

            int cnt = 0;
            while(x != 0)
            {
                if(x%2 == 1)
                {
                    cnt += 1;
                }
                x /= 2;
            }
            Console.WriteLine(cnt);
        }
    }
}
