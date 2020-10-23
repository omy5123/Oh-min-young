using System;

namespace _1543__문서_검색_
{
    class _1543
    {
        static void solution(string str, string ch)
        {
            int answer = 0;
            int idx = 0;
            if(str.Length == ch.Length)
            {
                bool check = false;
                for(int i = 0; i<str.Length;i++)
                {
                    if(str[i] != ch[i])
                    {
                        check = true;
                        break;
                    }
                }
                if(check == false)
                {
                    answer += 1;
                }
            }
            else if(str.Length < ch.Length)
            {
                answer = 0;
            }
            else
            {
                while (idx <= str.Length - 1)
                {
                    bool check = false;
                    for (int i = 0; i < ch.Length; i++)
                    {
                        if (ch[i] != str[idx])
                        {
                            if(i>0)
                            {
                                idx = idx + 1 - i;
                                check = true;
                                break;
                            }
                            idx += 1;
                            check = true;
                            break;
                        }
                        else
                        {
                            idx += 1;
                        }

                    }
                    if (check == false)
                    {
                        answer += 1;
                    }
                    if (str.Length - idx < ch.Length)
                    {
                        break;
                    }
                }
            }
            
            Console.WriteLine(answer);
        }
        static void Main(string[] args)
        {
            string str = Console.ReadLine();
            string ch = Console.ReadLine();
            solution(str, ch);
        }
    }
}
