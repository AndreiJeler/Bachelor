using Bachelor_Client.Entities;
using Bachelor_Client.Pose;
using Bachelor_Client.Utils;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Bachelor_Client
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main(string[] args)
        {
            Console.WriteLine(Directory.GetCurrentDirectory());
            ExerciseModel model = JsonConvert.DeserializeObject<ExerciseModel>(File.ReadAllText(@"kinect-config.json"));
            RunConfig config = JsonConvert.DeserializeObject<RunConfig>(File.ReadAllText(@"run-config.json"));
            model.CreateDictionaries();
            Exercise exercise = JointsOperations.CreateExerciseClass(model.Name, config.Reps);
            ActivityManager.CreateActivity(model.Id);
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainPage(model, config.Reps, exercise));
        }
    }
}
