using System;
using System.Text;

namespace _14888__연산자_끼워넣기_
{
    class _14888
    {
        static int max_result = int.MinValue;
        static int min_result = int.MaxValue;
        static int[] arr;
        static int n;
        static void dfs(int cnt, int result, int plus, int minus, int mul, int div)
        {
            if (cnt == n)
            {
                if (max_result < result)
                {
                    max_result = result;
                }
                if (min_result > result)
                {
                    min_result = result;
                }
            }
            else
            {
                if (plus != 0)
                {
                    dfs(cnt + 1, result + arr[cnt], plus - 1, minus, mul, div);
                }
                if (minus != 0)
                {
                    dfs(cnt + 1, result - arr[cnt], plus, minus - 1, mul, div);
                }
                if (mul != 0)
                {
                    dfs(cnt + 1, result * arr[cnt], plus, minus, mul - 1, div);
                }
                if (div != 0)
                {
                    dfs(cnt + 1, result / arr[cnt], plus, minus, mul, div - 1);
                }
            }
        }
        static void Main(string[] args)
        {
            n = int.Parse(Console.ReadLine());
            StringBuilder sb = new StringBuilder();
            
            string[] st = Console.ReadLine().Split();
            arr = new int[n];
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(st[i]);
            }
            string[] str = Console.ReadLine().Split();
            int[] op = new int[4];
            for (int i = 0; i < 4; i++)
            {
                op[i] = int.Parse(str[i]);
            }

            dfs(1, arr[0], op[0],op[1], op[2], op[3]);
            sb.Append(max_result).AppendLine();
            sb.Append(min_result).AppendLine();
            Console.WriteLine(sb);

        }
    }
}
