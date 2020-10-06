using System;

namespace _2644__촌수계산_
{
    class _2644
    {
        
        static int n;
        static int m;
        static int pe1;
        static int pe2;
        static bool check = false;

        static void dfs(int[,] arr, bool[] visit,int start,int cnt)
        {
            if (start == pe2)
            {
                check = true;
                Console.WriteLine(cnt);
                return;
            }
            else
            {
                for (int i = 1; i < n+1; i++)
                {
                    if (arr[start, i] == 1 && visit[i] == false)
                    {
                        visit[i] = true;
                        
                        
                        dfs(arr, visit, i,cnt + 1);
                        if(check)
                        {
                            return;
                        }
                    }
                }
            }
            
        }
        static void Main(string[] args)
        {
            n = int.Parse(Console.ReadLine());
            string[] people = Console.ReadLine().Split();
            pe1 = int.Parse(people[0]);
            pe2 = int.Parse(people[1]);
            m = int.Parse(Console.ReadLine());
            int[,] arr = new int[n + 1, n + 1];
            bool[] visit = new bool[n + 1];
            for (int i = 0; i < m; i++)
            {
                string[] xy = Console.ReadLine().Split();
                int x = int.Parse(xy[0]);
                int y = int.Parse(xy[1]);
                arr[x, y] = 1;
                arr[y, x] = 1;
            }
            dfs(arr, visit, pe1,0);
            if(!(check))
            {
                Console.WriteLine(-1);
            }
            

        }
    }
}
