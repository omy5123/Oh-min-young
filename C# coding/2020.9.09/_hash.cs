using System;
using System.Collections.Generic;
using System.Linq;

namespace _hash__완주하지_못한_선수_
{
    class _hash
    {
        string solution(string[] t,string[] c)
        {
            List<string> list = new List<string>(t);
            foreach (string i in c)
            {
                if (t.Contains(i))
                {
                    list.Remove(i);
                }
            }
            return list[0];
        }
        static void Main(string[] args)
        {
            string[] participant = { "leo", "kiki", "eden" };
            string[] completion = { "eden", "kiki" };
        }
    }
}
