using System;
using System.Collections.Generic;
using System.Text;

namespace _2263__트리의_순회_
{
    class _2263
    {
        static int n;
        static List<int> pre = new List<int>();
        static List<int> pos = new List<int>();
        static int[] inorder;
        static int[] postorder;
        static int root;
        static StringBuilder sb = new StringBuilder();
        static void divide(int in_start,int in_end,int post_start, int post_end)
        {
            if ((in_start > in_end) || (post_start > post_end))
            {
                return;
            }
            root = postorder[post_end]; //pos가 0부터 시작이라서

            sb.Append(root + " ");
            int p = pos[root];
            int left = p - in_start;
            divide(in_start, p - 1, post_start, post_start + left - 1);
            divide(p + 1, in_end, post_start +left, post_end - 1);

        }
        static void solution(int n, int[] inorder, int[] postorder)
        {
            for (int i = 0; i < n + 1; i++)
            {
                pos.Add(0);
            }


            for (int i = 0; i < n; i++)
            {
                pos[inorder[i]] = i;
            }

            divide(0, n - 1, 0, n - 1);
            Console.WriteLine(sb);
        }
        static void Main(string[] args)
        {
            n = int.Parse(Console.ReadLine());
            inorder = new int[n];
            string[] line = Console.ReadLine().Split();
            for (int i = 0; i < n; i++)
            {
                inorder[i] = int.Parse(line[i]);
            }
            postorder = new int[n];
            string[] line_1 = Console.ReadLine().Split();
            for (int i = 0; i < n; i++)
            {
                postorder[i] = int.Parse(line_1[i]);
            }
            solution(n, inorder, postorder);
        }
    }
}
