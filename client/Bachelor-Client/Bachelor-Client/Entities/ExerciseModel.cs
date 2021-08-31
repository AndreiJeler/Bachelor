using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bachelor_Client.Entities
{
   public class ExerciseModel
    {
        public string Id { get; set; }
        public string Name { get; set; }
        public string Difficulty { get; set; }
        public string EndPic { get; set; }
        public string StartPic { get; set; }
        public string BodyRegion { get; set; }
        public string Pic { get; set; }
        public string CorrectnessLabels { get; set; }
        public string CorrectnessExplanations { get; set; }
        public string RepsLabels { get; set; }
        public string RepsExplanations { get; set; }
        public string RepsModel { get; set; }
        public string CorrectnessModel { get; set; }
        public Dictionary<string, string> CorrectnessLabelsDict { get; set; }
        public Dictionary<string, string> CorrectnessExplanationsDict { get; set; }
        public Dictionary<string, string> RepsLabelsDict { get; set; }
        public Dictionary<string, string> RepsExplanationsDict { get; set; }

        public void CreateDictionaries()
        {
            RepsLabelsDict =  JsonConvert.DeserializeObject<Dictionary<string, string>>(RepsLabels);
            CorrectnessExplanationsDict = JsonConvert.DeserializeObject<Dictionary<string, string>>(CorrectnessExplanations);
            CorrectnessLabelsDict = JsonConvert.DeserializeObject<Dictionary<string, string>>(CorrectnessLabels);
            RepsExplanationsDict = JsonConvert.DeserializeObject<Dictionary<string, string>>(RepsExplanations);

        }
    }
}
