using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TumblrAngel
{
    class Logger
    {
        public static void PrintDebug(string msg)
        {
            DateTime time = System.DateTime.Now;
            Console.WriteLine(time.ToString());
        }

        public static void PrintMessage(string msg)
        {
            DateTime time = System.DateTime.Now;
            Console.WriteLine(time.ToString());
        }

        public static void PrinteError(string msg)
        {
            DateTime time = System.DateTime.Now;
            Console.WriteLine(time.ToString());
        }
    }
}
