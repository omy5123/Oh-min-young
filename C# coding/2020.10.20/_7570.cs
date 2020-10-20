using System;

namespace _7570__줄_세우기_
{
    class _7570
    {
        static int solution(int n, int[] arr)
        {
            int answer = 0;
            return answer;
        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string[] line = Console.ReadLine().Split();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(line[i]);
            }
            Console.WriteLine(solution(n, arr));
        }
    }
}
