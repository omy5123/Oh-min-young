using System;

namespace _price
{
    class _price
    {
        static int[] solution(int[] prices)
        {
            int[] result = new int[prices.Length];
            for (int i = 0; i < prices.Length; i++)
            {
                int cnt = 0;
                for (int j = i+1; j < prices.Length; j++)
                {
                    if (prices[i] <= prices[j])
                    {
                        cnt += 1;
                    }
                    else
                    {
                        cnt += 1;
                        break;
                    }
                }
                result[i] = cnt;
            }
            return result;
        }
        static void Main(string[] args)
        {
            int[] prices = { 1, 2, 3, 2, 3 };
            int []result = solution(prices);
        }
    }
}
