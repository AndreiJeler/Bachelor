using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bachelor_Client.Utils
{
    public class MistakesDictionary
    {
        public Dictionary<int, String> Mistakes { get; set; }
        
        public MistakesDictionary()
        {
            Mistakes = new Dictionary<int, string>();
        }

        public bool CheckRep(int rep)
        {
            return Mistakes.Keys.Contains(rep);
        }

        public bool AddMistake(int rep, string mistake)
        {
            if(!CheckRep(rep))
            {
                Mistakes.Add(rep, mistake);
                return true;
            }
            return false;
        }
    }
}
