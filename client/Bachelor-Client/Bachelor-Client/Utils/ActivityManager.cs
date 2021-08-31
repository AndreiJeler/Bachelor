using Bachelor_Client.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bachelor_Client.Utils
{
    public class ActivityManager
    {
        private static Activity _instance;

        public static void CreateActivity(string e_id)
        {
            ActivityManager._instance = new Activity { e_id = e_id, date = new DateTime(), sets = new List<Set>() };
        }

        public static void AddSet(Set set)
        {
            ActivityManager._instance.sets.Add(set);
        }

        public static Activity GetActivity()
        {
            return ActivityManager._instance;
        }

        public static void Reset()
        {
            ActivityManager._instance = new Activity {};
        }
    }
}
