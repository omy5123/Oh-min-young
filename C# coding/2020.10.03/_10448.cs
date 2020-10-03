using System;
using System.Collections.Generic;
using System.Text;

namespace _10448__유레카_이론_
{
    class _10448
    {
        static int k;
        static bool check;
        static StringBuilder sb = new StringBuilder();
        static void dfs(int cnt, int sum, int idx, List<int> list)
        {
            if(cnt == 3)
            {
                if(sum == k)
                {
                    check = true;
                    return;
                }
            }
            else
            {
                for (int i = idx; i < list.Count; i++)
                {
                    dfs(cnt + 1, sum + list[i], i, list);
                    if(check)
                    {
                        return;
                    }
                }
            }
        }
        static void Main(string[] args)
        {
            int t = int.Parse(Console.ReadLine());

            for (int i = 0; i < t; i++)
            {
                List<int> list = new List<int>();
                k = int.Parse(Console.ReadLine());
                check = false;
                int num = 1;
                while (num*(num+1)/2 < k)
                {
                    list.Add(num * (num + 1) / 2);
                    num += 1;
                }
                dfs(0, 0, 0, list);
                if (check)
                {
                    sb.Append(1).AppendLine();
                }
                else
                {
                    sb.Append(0).AppendLine();
                }
                
            }
            Console.WriteLine(sb);
        }
    }
}
