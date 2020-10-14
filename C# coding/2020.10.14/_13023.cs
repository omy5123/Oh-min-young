using System;
using System.Collections.Generic;
using System.Linq;

namespace _13023__ABCDE_
{
    class _13023
    {
        static List<List<int>> list = new List<List<int>>();
        static bool check;
        static void dfs(int i,bool[] visit,int k)
        {
            visit[i] = true;
            if (k == 4)
            {
                check = true;
                return;
            }
            for (int j = 0; j < list[i].Count; j++)
            {
                if (visit[list[i][j]] == false)
                {
                    dfs(list[i][j], visit,k+1);
                    visit[list[i][j]] = false;
                    if(check)
                    {
                        return;
                    }
                } 
            }
        }
        static void Main(string[] args)
        {
            string[] nm = Console.ReadLine().Split();
            int n = int.Parse(nm[0]);
            int m = int.Parse(nm[1]);
            for (int i = 0; i < n; i++)
            {
                list.Add(new List<int>());
            }
            for (int i = 0; i < m; i++)
            {
                string[] ab = Console.ReadLine().Split();
                int a = int.Parse(ab[0]);
                int b = int.Parse(ab[1]);
                list[a].Add(b);
                list[b].Add(a);
            }
            check = false;
            for (int i = 0; i < n; i++)
            {
                bool[] visit = new bool[n];
                dfs(i,visit,0);
                visit[i] = false;
                if (check)
                {
                    break;
                }
            }
            if(check)
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
