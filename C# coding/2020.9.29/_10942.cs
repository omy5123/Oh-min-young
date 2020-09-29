using System;
using System.Collections.Generic;
using System.Text;

namespace _10942__팰린드롬_
{
    class _10942
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string[] st = Console.ReadLine().Split();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(st[i]);
            }
            int m = int.Parse(Console.ReadLine());
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < m; i++)
            {
                Stack<int> stack = new Stack<int>();
                
                string[] se = Console.ReadLine().Split();
                int s = int.Parse(se[0]);
                int e = int.Parse(se[1]);
                for (int j = s - 1; j < e; j++)
                {
                    stack.Push(arr[j]);
                }
                bool check = true;
                for (int j = s-1; j < e; j++)
                {
                    if(stack.Pop() != arr[j])
                    {
                        check = false;
                        break;
                    }
                    else
                    {
                        continue;
                    }
                }
                if (check)
                {
                    sb.AppendLine("1");
                }
                else
                {
                    sb.AppendLine("0");
                }
                
                
            }
            Console.WriteLine(sb);
        }
    }
}
