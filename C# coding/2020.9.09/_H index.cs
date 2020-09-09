using System;

namespace _H_index
{
    class Program
    {
        static int solution(int[] citations)
        {
            
            int cnt = 0;
            Array.Sort(citations);
            
            for (int i = 1; i < citations.Length+1; i++)
            {
                int u = 0;
                int v = 0;
                for (int j = 0; j < citations.Length; j++)
                {
                    if (citations[j] >= i)
                    {
                        u += 1;
                    }
                    else if (citations[j] < i)
                    {
                        v += 1;
                    }

                }
                if (u>=i && v<=i)
                {
                    if (cnt < i)
                    {
                        cnt = i;
                    }
                }
            }
            
            return cnt;
        }
        static void Main(string[] args)
        {
            int[] citations = { 3, 0, 6, 1, 5 };
            Console.WriteLine(solution(citations));
        }
    }
}
