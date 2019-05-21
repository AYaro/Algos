using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace Week3
{
    public class Task1
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
            var prefixes = new int[str.Length];

            int k = 0;
            for (int i = 1; i < str.Length; ++i)
            {
                while (k > 0 && str[k] != str[i])
                {
                    k = prefixes[k - 1];
                }

                if (str[k] == str[i])
                {
                    k++;
                }

                prefixes[i] = k;
            }

            File.WriteAllText("output.txt", string.Join(" ", prefixes));
        }
    }
}
