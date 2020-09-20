using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace _10773
{
    class _10773
    {
        static void Main(string[] args)
        {
            Stack<int> stack = new Stack<int>();
            int k = int.Parse(Console.ReadLine());

            for (int i = 0; i < k; i++)
            {
                int k_k = int.Parse(Console.ReadLine());
                if (k_k == 0)
                {
                    stack.Pop();
                }
                else
                {
                    stack.Push(k_k);
                }
            }
            Console.WriteLine(stack.Sum());
        }
    }
}
