using System;
using System.Security.Cryptography.X509Certificates;

namespace _target_number
{
    public class _target
    {
        static int cnt = 0;
        static void Dfs(int[]arr, int target, int idx, int num)
        {
            if (idx == arr.Length)
            {
                if (target == num)
                {
                    cnt += 1;
                    return;
                }
                else
                {
                    return;
                }
            }
            else
            {
                Dfs(arr, target, idx + 1, num + arr[idx]);
                Dfs(arr, target, idx + 1, num - arr[idx]);
            }
        }
        static int solution(int[] numbers, int target)
        {
            Dfs(numbers,target,0,0);
            return cnt;
        }
        static void Main(string[] args)
        {
            int[] numbers = {1,1,1,1,1};
            int target = 3;
            int result = solution(numbers, target);
            Console.WriteLine(result);
        }
    }
}
