using System;
using System.Collections.Generic;
using System.Linq;

namespace _printer
{
    class _printer
    {
        static void solution(int[] ar, int lo)
        {
            int answer = 0;
            Queue<int> que = new Queue<int>();
            List<int> max = new List<int>(ar);
            for (int i = 0; i < max.Count; i++)
            {
                que.Enqueue(i);
            }
            while (que.Count!=0)
            {
                int a = que.Dequeue();
                if (max.Max() <= ar[a])
                {
                    answer += 1;
                    max.Remove(ar[a]);
                    if (a == lo)
                    {
                        break;
                    }
                }
                else
                {
                    que.Enqueue(a);
                }
            }
            Console.WriteLine(answer);
            
        }
        static void Main(string[] args)
        {
            int[] priorities = { 2, 1, 3, 2 };
            int location = 0;
            solution(priorities, location);
        }
    }
}
