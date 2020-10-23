using System;

namespace _10822__더하기_
{
    class _10822
    {
        static void solution(string str)
        {
            string[] line = str.Split(',');
            int sum = 0;
            foreach (var i in line)
            {
                sum += int.Parse(i);
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
