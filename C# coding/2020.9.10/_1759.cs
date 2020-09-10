using System;
using System.Collections.Generic;
using System.Linq;

namespace _1759__암호_만들기_
{
    
    class _1759
    {
        static int l = 0;
        static int c = 0;
        static string[] arr = new string[c];
        static bool[] flag = { };
        static List<string> ch = new List<string>();
        static List<string> str = new List<string>();
        static void dfs(int cnt,int idx)
        {
            if (cnt == l)
            {
                string s = "";
                for (int i = 0; i < l; i++)
                {
                    s += ch[i];
                }
                
                if (str.Contains(s) == false)
                {
                    str.Add(s);
                    return;
                }
            }
            else
            {
                for (int i = idx; i < c; i++)
                {
                    ch.Add(arr[i]);
                    dfs(cnt + 1,i+1);
                    ch.Remove(arr[i]);
                }
            }
        }
        static void check(List<string> str)
        {
            foreach (string i in str)
            {
                int u = 0;
                int v = 0;
                string s = "aeiou";
                for (int j = 0; j < i.Length; j++)
                {
                    if (s.Contains(i[j]))
                    {
                        u += 1;
                    }
                    else
                    {
                        v += 1;
                    }
                }
                if (u >= 1 && v >= 2)
                {
                    Console.WriteLine(i);
                }
            }
            return;
        }
           
        static void Main(string[] args)
        {
            string[] ar = Console.ReadLine().Split();
            l = int.Parse(ar[0]);
            c = int.Parse(ar[1]);
            arr = Console.ReadLine().Split();
            
            Array.Sort(arr);
            dfs(0,0);
            check(str);
            
        }
    }
}
