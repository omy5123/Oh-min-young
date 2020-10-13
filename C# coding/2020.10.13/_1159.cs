using System;
using System.Collections.Generic;

namespace _1159__농구_경기_
{
    class _1159
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            List<char> list = new List<char>();
            for (int i = 0; i < n; i++)
            {
                string str = Console.ReadLine();
                list.Add(str[0]);
            }
            int[] cnt = new int[26];
            for (int i = 0; i < n; i++)
            {
                cnt[(int)list[i] - 97] += 1;
            }
            bool check = false;
            for (int i = 0; i < 26; i++)
            {
                if (cnt[i] >= 5)
                {
                    check = true;
                    Console.Write((char)(i + 97));
                }
            }
            if (check==false)
            {
                Console.WriteLine("PREDAJA");
            }
            
        }
    }
}
