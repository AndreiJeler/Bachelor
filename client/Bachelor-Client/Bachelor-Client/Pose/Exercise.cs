using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Kinect;

namespace Bachelor_Client.Pose
{
    public abstract class Exercise
    {
        protected int _reps;
        protected int _goodReps;
        protected int _maxReps;
        protected String _currentStage;
        protected bool isError;

        public Exercise(int reps)
        {
            _maxReps = reps;
            _reps = 0;
            _goodReps = 0;
            _currentStage = "None";
        }

        public virtual KeyValuePair<string, int> CheckRepetition(JointCollection joints)
        {
            if (_currentStage == "None")
            {
                if (IsStart(joints))
                {
                    _currentStage = "start";
                }
            }

            else if (_currentStage == "start")
            {
                if (IsEnd(joints))
                {
                    _currentStage = "end";
                }
            }
            else if (_currentStage == "end")
            {
                if (IsStart(joints))
                {
                    _currentStage = "start";
                    _reps++;
                    if(!isError)
                    {
                        _goodReps += 1;
                    }
                    isError = false;
                }
            }

            return new KeyValuePair<string, int>(_currentStage, _reps);
        }

        public bool IsDone()
        {
            return _reps >= _maxReps;
        }

        public abstract bool IsStart(JointCollection joints);
        public abstract bool IsEnd(JointCollection joints);

        public abstract KeyValuePair<int,string> CheckErrors(JointCollection joints);

        protected float GetDistanceX(Joint j1, Joint j2)
        {
            return Math.Abs(j1.Position.X - j2.Position.X);
        }

        protected float GetDistanceY(Joint j1, Joint j2)
        {
            return Math.Abs(j1.Position.Y - j2.Position.Y);
        }

        protected float GetDistanceZ(Joint j1, Joint j2)
        {
            return Math.Abs(j1.Position.Z - j2.Position.Z);
        }

        public int GetReps()
        {
            return _reps;
        }

        public int GetGoodReps()
        {
            return _goodReps;
        }
    }
}
