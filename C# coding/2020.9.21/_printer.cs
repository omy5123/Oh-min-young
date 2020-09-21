using System;
using System.Collections.Generic;
using System.Linq;

namespace _printer
{
    class _printer
    {
        static int solution(int[] ar, int lo)
        {
            int result = 0;
            Queue<int> que = new Queue<int>();
            List<int> prior = new List<int>(ar);

            for (int i = 0; i < ar.Length; i++)
            {
                que.Enqueue(i);
            }
            while (true)
            {
                int a = que.Dequeue();
                if (prior.Max() == ar[a])
                {
                    result += 1;
                    prior.Remove(ar[a]);
                    if (a == lo)
                    {
                        return result;
                    }

                }
                else
                {
                    que.Enqueue(a);
                }
            }

        }
        static void Main(string[] args)
        {
            int[] priorities = { 2, 1, 3, 2 };
            int location = 2;
            Console.WriteLine(solution(priorities, location));
        }
    }
}
