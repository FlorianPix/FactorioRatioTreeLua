using Newtonsoft.Json;
using System;
using System.IO;

namespace RecipeReader
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            using (StreamReader r = new StreamReader("file.json"))
            {
                string json = r.ReadToEnd();
                dynamic array = JsonConvert.DeserializeObject(json);
                foreach (var item in array)
                {
                    Console.WriteLine("{0} {1}", item.temp, item.vcc);
                }
            }
        }
    }
}
