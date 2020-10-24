using System;

namespace _1225__이상한_곱셈_
{
    class Program
    {
        static void solution(string str)
        {
            long sum = 0;
            string[] line = str.Split();
            string a = line[0];
            string b = line[1];
            for (int i = 0; i < a.Length; i++)
            {
                for (int j = 0; j < b.Length; j++)
                {
                    sum += ((int)a[i]-48) * ((int)b[j] - 48);
                }
            }
            Console.WriteLine(sum);

        }
        static void Main(string[] args)
        {
            string str = Console.ReadLine();
            solution(str);
        }
    }
}
