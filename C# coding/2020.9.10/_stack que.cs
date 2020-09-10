using System;
using System.Collections.Generic;

namespace _stack_que__기능개발_
{
    class _stack_que
    {
        static void solution(int[] progresses, int[] speeds)
        {
            List<int> list = new List<int>();
            int count = 1;
            int cn = 0;
            while (progresses[0] < 100)
            {
                progresses[0] += speeds[0];
                cn += 1;
            }
            int max = cn;

            for (int i = 1; i < progresses.Length; i++)
            {
                int a = progresses[i];
                int cnt = 0;
                while (a < 100)
                {
                    a += speeds[i];
                    cnt += 1;
                }
                if (max >= cnt)
                {
                    count += 1;
                }
                else
                {
                    list.Add(count);
                    count = 1;
                    max = cnt;
                }
            }
            list.Add(count);
            for (int i = 0; i < list.Count; i++)
            {
                Console.WriteLine(list[i]);
            }
            
        }
        static void Main(string[] args)
        {
            int[] progresses = { 95, 90, 99, 99, 80, 99 };
            int[] speeds = { 1, 1, 1, 1, 1, 1 };
            solution(progresses, speeds);
        }
    }
}
