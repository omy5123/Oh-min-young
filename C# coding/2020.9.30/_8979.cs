using System;
using System.Collections.Generic;
using System.Linq;

namespace _8979__올림픽_
{
    class _8979
    {
        struct Cor
        {
            public int rank;
            public int gold;
            public int sliver;
            public int bronze;

        }
        static void Main(string[] args)
        {
            string[] nk = Console.ReadLine().Split();
            int n = int.Parse(nk[0]);
            int k = int.Parse(nk[1]);
            Cor[] medal = new Cor[n];
            for (int i = 0; i < n; i++)
            {
                string[] str = Console.ReadLine().Split();
                medal[i].rank = int.Parse(str[0]);
                medal[i].gold = int.Parse(str[1]);
                medal[i].sliver = int.Parse(str[2]);
                medal[i].bronze = int.Parse(str[3]);
            }
            Array.Sort(medal, delegate(Cor u, Cor v)
            {
                if(u.gold > v.gold)
                {
                    return -1;
                }
                else if (u.gold < v.gold)
                {
                    return 1;
                }
                else
                {
                    if (u.sliver > v.sliver)
                    {
                        return -1;
                    }
                    else if (u.sliver < v.sliver)
                    {
                        return 1;
                    }
                    else
                    {
                        if (u.bronze > v.bronze)
                        {
                            return -1;
                        }
                        else if (u.bronze < v.bronze)
                        {
                            return 1;
                        }
                        else
                        {
                            return 0;
                        }
                    }
                }
            });

            int a = 0;
            int b = 0;
            int c = 0;

            int result = 1;
            for (int i = 0; i < n; i++)
            {
                if(medal[i].rank == k)
                {
                    a = medal[i].gold;
                    b = medal[i].sliver;
                    c = medal[i].bronze;
                    break;
                }
            }
            for (int i = 0; i < n; i++)
            {
                if (medal[i].gold == a && medal[i].sliver == b && medal[i].bronze == c)
                {
                    Console.WriteLine(result);
                    break;
                }
                else
                {
                    result += 1;
                }
            }
         
        }

    }
}
