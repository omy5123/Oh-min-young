using System;

namespace _13305__주유소_
{
    class _13305
    {
        static void Main(string[] args)
        {
            long n = int.Parse(Console.ReadLine());
            string[] distance = Console.ReadLine().Split();
            long[] dist = new long[distance.Length];
            for (int i = 0; i < distance.Length; i++)
            {
                dist[i] = long.Parse(distance[i]);
            }
            string[] price = Console.ReadLine().Split();
            long[] p = new long[price.Length];
            for (int i = 0; i < price.Length; i++)
            {
                p[i] = int.Parse(price[i]);
            }

            long result = p[0] * dist[0];
            long min = p[0];
            for (int i = 1; i < dist.Length; i++)
            {
                if (min > p[i])
                {
                    min = p[i];
                    result += min * dist[i];
                }
                else
                {
                    result += min * dist[i];
                }
            }
            Console.WriteLine(result);

        }
    }
}
