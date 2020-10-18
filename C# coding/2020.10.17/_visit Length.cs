using System;
using System.Collections.Generic;

namespace _visit_Length
{
    class Program
    {
        static int solution(string dirs)
        {
            int[] dx = { -1, 0, 1, 0 };
            int[] dy = { 0, -1, 0, 1 };
            Dictionary<char, int> d = new Dictionary<char, int>()
            {
                {'U',0},
                {'L',1},
                {'D',2},
                {'R',3}
            };
            int cnt = 0;
            SortedSet<(int, int, int, int)> visited = new SortedSet<(int, int, int, int)>();
            int x = 0;
            int y = 0;
            foreach (var i in dirs)
            {
                int a = x + dx[d[i]];
                int b = y + dy[d[i]];
                if ((-5 <= a && a<=5) && (-5 <= b && b <= 5))
                {
                    if(visited.Contains((x, y, a, b)) == false)
                    {
                        visited.Add((x, y, a, b));
                        visited.Add((a, b, x, y));
                        cnt += 1;
                    }
                    
                    x = a;
                    y = b;
                }
                else
                {
                    continue;
                }


            }
            return cnt;
        }
        static void Main(string[] args)
        {
            string dirs = "LULLLLLLU";
            Console.WriteLine(solution(dirs));

        }
    }
}
