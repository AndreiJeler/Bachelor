using Bachelor_Client.Entities;
using Microsoft.Kinect;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Keras;

namespace Bachelor_Client.Pose
{
    public class ExerciseNN : Exercise
    {
        private string _exerciseName;
        private string _repsModelLoc;
        private string _correctnessModelLoc;
        private ExerciseModel _exerciseModel;
        private Keras.Models.BaseModel _repsModel;
        private Keras.Models.BaseModel _correctnessModel;
        private int _currentFrame;

        public ExerciseNN(int reps, string exerciseName, string corrModelLocation, string repsModelLocation, ExerciseModel model) : base(reps)
        {
            _exerciseName = exerciseName;
            _repsModelLoc = repsModelLocation;
            _correctnessModelLoc = corrModelLocation;
            _exerciseModel = model;
            _repsModel = Keras.Models.Model.LoadModel(_repsModelLoc);
            _correctnessModel = Keras.Models.Model.LoadModel(_correctnessModelLoc);
            _currentFrame = 0;
        }

        public override KeyValuePair<string, int> CheckRepetition(JointCollection joints)
        {
            var newState = CheckRepetitionStatusML(joints);
            if (_currentStage == "None")
            {
                if (newState == "start")
                {
                    _currentStage = "start";
                }
            }

            else if (_currentStage == "start")
            {
                if (newState == "end")
                {
                    _currentStage = "end";
                }
            }
            else if (_currentStage == "end")
            {
                if (newState == "start")
                {
                    _currentStage = "start";
                    _reps++;
                    if (!isError)
                    {
                        _goodReps += 1;
                    }
                    isError = false;
                }
            }

            return new KeyValuePair<string, int>(_currentStage, _reps);
        }

        public override KeyValuePair<int, string> CheckErrors(JointCollection joints)
        {
            throw new NotImplementedException();
        }

        public override bool IsEnd(JointCollection joints)
        {
            throw new NotImplementedException();
        }

        public override bool IsStart(JointCollection joints)
        {
            throw new NotImplementedException();
        }

        private string CheckRepetitionStatusML(JointCollection joints)
        {
            _currentFrame += 1;
            if (_currentFrame % 5 != 0)
            {
                return _currentStage;
            }
            if (_exerciseName != "Squats")
            {
                //Luate pt arms
            }
            return "end";
        }
    }
}
