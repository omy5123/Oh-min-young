using Microsoft.VisualBasic.CompilerServices;
using System;
using System.Linq;
using System.Text;

namespace _10815__숫자_카드_
{
    class _10815
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string[] ar = Console.ReadLine().Split();
            int[] arr = new int[n];
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(ar[i]);
            }
            int m = int.Parse(Console.ReadLine());
            string[] br = Console.ReadLine().Split();
            int[] brr = new int[m];
            for (int i = 0; i < m; i++)
            {
                brr[i] = int.Parse(br[i]);
            }
            string str = "";
            foreach (var i in brr)
            {
                if (arr.Contains(i) == true)
                {
                    sb.Append("1 ");
                }
                else
                {
                    sb.Append("0 ");
                }
            }
            Console.WriteLine(sb);

            /*int n = int.Parse(Console.ReadLine());
            string[] ar = Console.ReadLine().Split();
            int[] arr = new int[n];
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(ar[i]);
            }
            int m = int.Parse(Console.ReadLine());
            string[] br = Console.ReadLine().Split();
            int[] brr = new int[m];
            for (int i = 0; i < m; i++)
            {
                brr[i] = int.Parse(br[i]);
            }
            Array.Sort(arr);
            
            foreach (var i in brr)
            {
                int low = 0;
                int high = n - 1;
                bool check = false;
                while (low <= high)
                {
                    int mid = (low + high) / 2;
                    if (arr[mid] == i)
                    {
                        sb.Append("1 ");
                        check = true;
                        break;
                    }
                    else if (arr[mid] <= i)
                    {
                        low = mid + 1;
                    }
                    else
                    {
                        high = mid - 1;
                    }
                }
                if (!(check))
                {
                    sb.Append("0 ");
                }
                
            }
            Console.WriteLine(sb);
            */
        }
    }
}
