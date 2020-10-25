using System;

namespace _14697__방_배정하기_
{
    class _14697
    {
        static bool state = false;
        static void backtracking(int n, int k,int[] rooms)
        {
            if (n == 0)
            {
                state = true;
            }
            
            else
            {
                if(k<3)
                {
                    for(int i = n/rooms[k];i>=0;i--)
                    {
                        backtracking(n - (rooms[k] * i), k + 1, rooms);
                        if(state)
                        {
                            break;
                        }
                    }
                }
            }
        }
        static void Main(string[] args)
        {
            string[] abcn = Console.ReadLine().Split();
            int a = int.Parse(abcn[0]);
            int b = int.Parse(abcn[1]);
            int c = int.Parse(abcn[2]);
            int n = int.Parse(abcn[3]);

            int[] rooms = { a, b, c };

            backtracking(n, 0,rooms);
            if(state)
            {
                Console.WriteLine(1);
            }
            else
            {
                Console.WriteLine(0);
            }
        }
    }
}
