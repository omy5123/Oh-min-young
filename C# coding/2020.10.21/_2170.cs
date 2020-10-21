using System;
using System.Collections.Generic;
using System.Linq;

namespace _2170
{
    class Program
    {
        struct Cor
        {
            public int Item1;
            public int Item2;
        }
        static int solution(int n, int[,] arr)
        {
            int answer = 0;
            /*List<Tuple<int, int>> list = new List<Tuple<int, int>>();
            for (int i = 0; i < n; i++)
            {
                list.Add(new Tuple<int, int>(arr[i, 0], arr[i, 1]));
            }
            list = list.OrderBy(x => x).ToList();*/
            Cor[] list = new Cor[n];
            for (int i = 0; i < n; i++)
            {
                list[i].Item1 = arr[i, 0];
                list[i].Item2 = arr[i, 1];
            }
            Array.Sort(list, delegate (Cor u, Cor v)
            {
                if(u.Item1 < v.Item1)
                {
                    return -1;
                }
                else if(u.Item1 > v.Item1)
                {
                    return 1;
                }
                else
                {
                    if(u.Item2 < v.Item2)
                    {
                        return -1;
                    }
                    else if(u.Item2 > v.Item2)
                    {
                        return 1;
                    }
                    else
                    {
                        return 0;
                    }
                }
            });
            int start = list[0].Item1;
            int end = list[0].Item2;
            answer += end - start;
            for (int i = 1; i < n; i++)
            {
                if (end > list[i].Item1 && end < list[i].Item2)
                {
                    answer += list[i].Item2 - end;
                    start = end;
                    end = list[i].Item2;
                }
                else if (end <= list[i].Item1)
                {
                    answer += list[i].Item2 - list[i].Item1;
                    start = list[i].Item1;
                    end = list[i].Item2;
                }
            }
            return answer;
        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int[,] arr = new int[n, 2];
            for (int i = 0; i < n; i++)
            {
                string[] line = Console.ReadLine().Split();
                arr[i, 0] = int.Parse(line[0]);
                arr[i, 1] = int.Parse(line[1]);
            }
            Console.WriteLine(solution(n, arr));
        }
    }
}
