using System;

namespace _joystick
{
    class _joystick
    {
        static int solution(string name)
        {
            int answer = 0;
            char[] chname = name.ToCharArray();
            string str = "";
            for (int i = 0; i < name.Length; i++)
            {
                str += 'A';
            }
            int idx = 0;
            while (true)
            {
                int right = 1;
                int left = 1;
                if (chname[idx] != 'A')
                {
                    
                    if ((int)chname[idx] - (int)'A' > 13)
                        answer += 26 - ((int)chname[idx] - (int)'A');
                    else
                        answer += (int)chname[idx] - (int)'A';
                    chname[idx] = 'A';
                }
                string ch = string.Join("", chname);
                if (str == ch)
                {
                    break;
                }
                else
                {
                    for (int i = 1; i < chname.Length; i++)
                    {
                        if (chname[idx + i] == 'A')
                        {
                            right += 1;
                        }
                        else
                        {
                            break;
                        }
                        if(idx-i ==0)
                        {
                            if (chname[chname.Length + (idx - i)] == 'A')
                            {
                                left += 1;
                            }
                        }
                        else
                        {
                            if (chname[idx - i] == 'A')
                            {
                                left += 1;
                            }
                        }
                        

                    }
                    if (right > left)
                    {
                        answer += left;
                        idx = chname.Length-left;
                    }
                    else
                    {
                        answer += right;
                        idx += right;
                    }
                }

            }
            return answer;
        }
        static void Main(string[] args)
        {
            string name = "BBBAAAB";
            int result = solution(name);
            Console.WriteLine(result);
        }
    }
}
