using System;

namespace _1339__단어_수학_
{
    class _1339
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            var arr = new string[n];
            var alphabets = new int[26];
            for (int i = 0; i < n; i++)
            {
                string line = Console.ReadLine();
                
                for (int j = 0; j < line.Length; j++)
                {
                    Console.WriteLine(alphabets[line[j] - 'A']);
                    alphabets[line[j] - 'A'] += (int)Math.Pow(10, line.Length - 1 - j);
                }
            }

            Array.Sort(alphabets, (a, b) => a < b ? 1 : a == b ? 0 : -1);

            int num = 9;
            int result = 0;
            for (int i = 0; i < alphabets.Length; i++)
            {
                if (alphabets[i] <= 0)
                {
                    break;
                }
                result += (alphabets[i] * num--);
            }

            Console.WriteLine(result);
        }
    }
}
