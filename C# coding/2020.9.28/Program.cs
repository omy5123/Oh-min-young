using System;
using System.Collections.Generic;
using System.Text;

namespace _4949__균형잡힌_세상_
{
    class Program
    {
        static void Main(string[] args)
        {
            Stack<string> stack = new Stack<string>();
            StringBuilder sb = new StringBuilder();
            while (true)
            {
                stack.Clear();
                string str = Console.ReadLine();
                if (str == ".")
                {
                    break;
                }
                else
                {
                    bool check = true;
                    for (int i = 0; i < str.Length; i++)
                    {
                        if (str[i].ToString() == "(")
                        {
                            stack.Push(str[i].ToString());
                        }
                        else if (str[i].ToString() == "[")
                        {
                            stack.Push(str[i].ToString());
                        }
                        else if (str[i].ToString() == ")")
                        {
                            if (stack.Count == 0)
                            {
                                check = false;
                                break;
                            }
                            else if (stack.Pop() == "(")
                            {
                                continue;
                            }
                            else
                            {
                                check = false;
                                break;
                            }
                        }
                        else if (str[i].ToString() == "]")
                        {
                            if (stack.Count == 0)
                            {
                                check = false;
                                break;
                            }
                            else if (stack.Pop() == "[")
                            {
                                continue;
                            }
                            else
                            {
                                check = false;
                                break;
                            }
                        }
                        else
                        {
                            continue;
                        }
                    }
                    if (stack.Count == 0 && check)
                    {
                        sb.AppendLine("yes");
                    }
                    else
                    {
                        sb.AppendLine("no");
                    }
                }
            }
            Console.WriteLine(sb);
        }
    }
}
