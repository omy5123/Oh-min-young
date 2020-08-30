using System;
using System.Text;

namespace _1316__그룹_단어_체커_
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int cnt = 0;
            for (int i = 0; i < n; i++)
            {
                string str = Console.ReadLine();
                string s = "";

                bool a = true;
                s += str[0];
                for (int j = 1; j < str.Length; j++)
                {
                    if (s[s.Length-1] != str[j])
                    {
                        foreach (char st in s)
                        {
                            if (st == str[j])
                            {
                                a = false;
                                break;
                            }
                        }
                    }
                    s += str[j];
                }
                if (a == true)
                {
                    cnt += 1;
                }

            }
            Console.WriteLine(cnt);
            
            
        }
    }
}
