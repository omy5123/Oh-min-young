using System;
using System.Linq;

namespace _1157__문자열_
{
    class Program
    {
        static void Main(string[] args)
        {
            string str = Console.ReadLine();
            str = str.ToUpper();
            int[] cnt = new int[26];
            
            for (int j = 0; j < str.Length; j++)
            {
                for (int i = 0; i< 26;i++)
                {
                    if (str[j] == (char)(65+i))
                    {
                        cnt[i]++;
                    }
                }
            }
            int result = cnt.Max();
            int s = 0;
            for (int i = 0; i < 26; i++)
            {
                if (result == cnt[i])
                {
                    s += 1;
                }
            }
            if (s == 1)
            {
                for (int i = 0; i < 26; i++)
                {
                    if (cnt[i] == result)
                    {
                        Console.WriteLine((char)(65 + i));
                    }
                }
            }
            else
            {
                Console.WriteLine("?");
            }
            
        }
    }
}
