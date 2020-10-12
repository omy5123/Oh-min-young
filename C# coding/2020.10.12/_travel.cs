using System;
using System.Security.Cryptography.X509Certificates;
using System.Linq;
using System.Collections.Generic;

namespace _travel
{
    class _travel
    {
        struct Cor
        {
            public string x;
            public string y;
        }
        static string[] solution(string[,] tickets)
        {
            
            Cor[] ticket = new Cor[tickets.GetLength(0)];
            for (int i = 0; i<tickets.GetLength(0);i++)
            {
                ticket[i].x = tickets[i, 0];
                ticket[i].y = tickets[i, 1];
            }
            Array.Sort(ticket, delegate (Cor u, Cor v)
            {
                return u.y.CompareTo(v.y);
            });
            Array.Sort(ticket,delegate(Cor u, Cor v)
            {
                return u.x.CompareTo(v.x);
            });
            Array.Reverse(ticket);
            Dictionary<string, List<string>> routes = new Dictionary<string, List<string>>();
            for (int i = 0; i < ticket.GetLength(0); i++)
            {
                string t1 = ticket[i].x;
                string t2 = ticket[i].y;
                if (routes.ContainsKey(t1))
                {
                    routes[t1].Add(t2);
                }
                else
                {
                    routes[t1] = new List<string> { t2 };
                }
            }
            Stack<string> stack = new Stack<string>();
            stack.Push("ICN");
            List<string> ans = new List<string>();
            while (stack.Count != 0)
            {
                string top = stack.Peek();
                if (routes.ContainsKey(top) == false || routes[top].Count == 0 )
                {
                    ans.Add(stack.Pop());
                }
                else
                {
                    stack.Push(routes[top][routes[top].Count - 1]);
                    routes[top].RemoveAt(routes[top].Count - 1);
                }
            }
            string[] an = ans.ToArray();
            Array.Reverse(an);

            
            return an;
        }
        static void Main(string[] args)
        {
            string[,] tickets = { { "ICN", "A" }, { "ICN", "B" }, { "B", "ICN" } };
            Console.WriteLine(string.Join(" ",solution(tickets)));
        }

    }
}
