using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace Week3
{
    public class task2
    {
        private static string[] input;
        private static int currentIndex;

        private static string ReadLine()
        {
            return input[currentIndex++];
        }

        public static void Main(string[] args)
        {
            input = File.ReadAllLines("input.txt");

            string str = ReadLine();
            int[] z = new int[str.Length];

            int L = 0, R = 0;
            for (int i = 1; i < str.Length; i++)
            {
                if (i > R)
                {
                    L = R = i;
                    while (R < str.Length && str[R - L] == str[R])
                    {
                        R++;
                    }

                    z[i] = R - L;
                    R--;
                }
                else
                {
                    int k = i - L;
                    if (z[k] < R - i + 1)
                    {
                        z[i] = z[k];
                    }
                    else
                    {
                        L = i;
                        while (R < str.Length && str[R - L] == str[R]) R++;
                        z[i] = R - L; R--;
                    }
                }
            }

            File.WriteAllText("output.txt", string.Join(" ", z.Skip(1)));
        }
    }
}
