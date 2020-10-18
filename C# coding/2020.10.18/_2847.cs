using System;

namespace _2847__게임을_만든_동준이_
{
    class _2847
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(Console.ReadLine());
            }
            int cnt = 0;
            for(int i = n-1; i>0;i--)
            {
                if(arr[i]<=arr[i-1])
                {
                    cnt += arr[i - 1] - arr[i] + 1;
                    arr[i - 1] = arr[i] - 1;
                }
            }
            Console.WriteLine(cnt);
        }
    }
}
