using System;
using System.Collections.Generic;
using System.Text;
namespace _1918__후위_표기식_
{
    class _1918
    {
        static void Main(string[] args)
        {
            Stack<char> stack = new Stack<char>();
            StringBuilder sb = new StringBuilder();
            Dictionary<char, int> priority = new Dictionary<char, int>()
            {
                {'*',2 },
                {'/',2},
                {'+',1 },
                {'-',1 },
                {'(',0 }
            };
            string alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            string str = Console.ReadLine();
            str = '(' + str + ')';
            foreach (var i in str)
            {
                if (alpha.Contains(i) == true)
                {
                    sb.Append(i);
                }
                else if (i == '(')
                {
                    stack.Push(i);
                }
                else if (i == ')')
                {
                    while (true)
                    {
                        char st = stack.Pop();
                        if (st == '(')
                        {
                            break;
                        }
                        sb.Append(st);
                    }
                }
                else
                {
                    while (stack.Peek() != '(' && priority[i] <= priority[stack.Peek()])
                    {
                        sb.Append(stack.Pop());
                    }
                    stack.Push(i);
                }

            }
            Console.WriteLine(sb);
        }
    }
}
