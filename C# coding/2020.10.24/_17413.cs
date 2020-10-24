using System;
using System.Text;
using System.Collections.Generic;

namespace _17413__단어_뒤집기2_
{
    class Program
    {
        static void solution(string str)
        {

            StringBuilder sb = new StringBuilder();
            Stack<string> stack = new Stack<string>();
            int idx = 0;
            while (idx < str.Length)
            {
                if (str[idx] == '<')
                {
                    while (str[idx] != '>')
                    {
                        sb.Append(str[idx]);
                        idx += 1;
                    }
                    sb.Append('>');
                    idx += 1;
                }
                else
                {
                    while (true)
                    {
                        if(idx == str.Length)
                        {
                            break;
                        }
                        if (str[idx] == '<' || str[idx] == ' ')
                        {
                            break;
                        }
                        else
                        {
                            stack.Push(str[idx].ToString());
                            idx += 1;
                        }
                    }
                    if(idx == str.Length)
                    {
                        while (stack.Count != 0)
                        {
                            sb.Append(stack.Pop());
                        }
                    }
                    else if (str[idx] == ' ')
                    {
                        while (stack.Count != 0)
                        {
                            sb.Append(stack.Pop());
                        }
                        sb.Append(' ');
                        idx += 1;
                    }
                    else if (str[idx] == '<')
                    {
                        while (stack.Count != 0)
                        {
                            sb.Append(stack.Pop());
                        }
                    }
                }
            }
            Console.WriteLine(sb);
        }
        static void Main(string[] args)
        {
            string str = Console.ReadLine();
            solution(str);
        }

    }
}
