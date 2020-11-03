using System;
using System.Collections.Generic;
using System.Text;

namespace _4256__트리_
{
    class _4256
    {
        static StringBuilder sb = new StringBuilder();
        static void post(int[] preorder, int[] inorder)
        {
            if(preorder.Length == 0)
            {
                return;
            }
            int root = preorder[0];
            int size = preorder.Length;

            int L = 0;
            for (int i = 0; i < size; i++)
            {
                if(inorder[i] == root)
                {
                    L = i;
                    break;
                }    
            }

            int R = size - L - 1;

            ArraySegment<int> pre = new ArraySegment<int>(preorder, 1, L);
            int[]preo = pre.ToArray();
            ArraySegment<int> ino = new ArraySegment<int>(inorder, 0, L);
            int[]inor = ino.ToArray();
            
            post(preo,inor);
            ArraySegment<int> pre_1 = new ArraySegment<int>(preorder, L+1, R);
            int[] preo_1 = pre_1.ToArray();
            ArraySegment<int> ino_1 = new ArraySegment<int>(inorder, L+1, R);
            int[] inor_1 = ino_1.ToArray();
            post(preo_1, inor_1);

            sb.Append(root + " ");

        }
        static void Main(string[] args)
        {
            int t = int.Parse(Console.ReadLine());
            
            for (int i = 0; i < t; i++)
            {
                int n = int.Parse(Console.ReadLine());
                
                int[] preorder = new int[n];
                int[] inorder = new int[n];
                string[] preline = Console.ReadLine().Split();
                for (int j = 0; j < n; j++)
                {
                    preorder[j] = int.Parse(preline[j]);
                }
                string[] inline = Console.ReadLine().Split();
                for (int j = 0; j < n; j++)
                {
                    inorder[j] = int.Parse(inline[j]);
                }
                post(preorder, inorder);
                sb.AppendLine();
                
            }
            Console.WriteLine(sb);
        }
    }
}
