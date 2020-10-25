using System;
using System.Linq;
using System.Collections.Generic;
using System.Numerics;

namespace _1251__단어_나누기_
{
    class _1251
    {
        static string Reverse(string s)
        {
            char[] charArray = s.ToCharArray();
            Array.Reverse(charArray);
            return new string(charArray);
        }
        static void Main(string[] args)
        {
            string str = Console.ReadLine();

            int N = str.Length;

            int k = 0;
            string minStr = null;
            for (int i = 1; i <= N - 2; i++)
            {
                for (int j = 1; j <= N - i - 1; j++)
                {
                    k = (N - i - j);

                    string str1 = Reverse(str.Substring(0, i));
                    string str2 = Reverse(str.Substring(i, j));
                    string str3 = Reverse(str.Substring(i + j));
                    string total = str1 + str2 + str3;
                    if (minStr == null)
                    {
                        minStr = total;
                    }
                    else
                    {
                        if (minStr.CompareTo(total) > 0)
                            minStr = total;
                    }
                }
            }
            Console.WriteLine(minStr);
        }
    }
}
