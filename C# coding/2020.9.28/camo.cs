using Microsoft.VisualBasic;
using System;
using System.Collections.Generic;

namespace _위장
{
    class camo
    {
        static int solution(string[,] clothes)
        {
            int answer = 1;
            Dictionary<string, int> dic = new Dictionary<string, int>();
            // 같은 종류끼리 건수 카운트
            for (int i = 0; i < clothes.GetLength(0); i++)
            {
                string strName = clothes[i, 0];
                string strType = clothes[i, 1];
                if (dic.ContainsKey(strType)) dic[strType]++;
                else dic.Add(strType, 1);
            }
            foreach (var item in dic)
            {
                answer *= (item.Value + 1);
            }
            return answer - 1;  // 의상을 한개는 걸쳐야 한다
        }
        static void Main(string[] args)
        {
            string[,] clothes = { { "yellow_hat", "headgear" }, { "blue_sunglasses", "eyewear" }, { "green_turban", "headgear" } };
            Console.WriteLine(solution(clothes));

        }
    }
}
