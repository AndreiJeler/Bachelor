using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Bachelor_Client.Utils;
using Microsoft.Kinect;

namespace Bachelor_Client.Pose
{
    public class BicepCurl : Exercise
    {

        private Stopwatch _time = new Stopwatch();
        private bool _isTooFast = false;
        private Joint _startLeftElbowPosition;
        private Joint _startRightElbowPosition;
        private bool _hasStarted = false;

        public BicepCurl(int reps) : base(reps)
        {
        }

        public override bool IsStart(JointCollection joints)
        {
            var angleLeft = JointsOperations.Get2DAngle(joints[JointType.ShoulderLeft],
                joints[JointType.ElbowLeft],
                joints[JointType.WristLeft]);

            var angleRight = JointsOperations.Get2DAngle(joints[JointType.ShoulderRight],
                joints[JointType.ElbowRight],
                joints[JointType.WristRight]);



            if (angleLeft >= 155
                   && angleRight >= 155
                   && joints[JointType.WristRight].Position.Y < joints[JointType.ElbowRight].Position.Y
                   && joints[JointType.WristLeft].Position.Y < joints[JointType.ElbowLeft].Position.Y)
            {
                if (_time.IsRunning)
                {
                    _time.Stop();
                    if (_time.ElapsedMilliseconds < 1000)
                    {
                        _isTooFast = true;
                    }
                }
                _time = new Stopwatch();
                _time.Start();

                _startRightElbowPosition = joints[JointType.ElbowRight];
                _startLeftElbowPosition = joints[JointType.ElbowLeft];
                _hasStarted = true;
                return true;
            }
            return false;
        }

        public override bool IsEnd(JointCollection joints)
        {
            var angleLeft = JointsOperations.Get2DAngle(joints[JointType.ShoulderLeft],
                joints[JointType.ElbowLeft],
                joints[JointType.WristLeft]);

            var angleRight = JointsOperations.Get2DAngle(joints[JointType.ShoulderRight],
                joints[JointType.ElbowRight],
                joints[JointType.WristRight]);

            return angleLeft <= 45
                   && angleRight <= 45
                   && joints[JointType.WristRight].Position.Y > joints[JointType.ElbowRight].Position.Y
                   && joints[JointType.WristLeft].Position.Y > joints[JointType.ElbowLeft].Position.Y;
        }

        public override KeyValuePair<int, string> CheckErrors(JointCollection joints)
        {
            if (_isTooFast)
            {
                _isTooFast = false;
                isError = true;
                return new KeyValuePair<int, string>(0, "You are doing the exercise too fast, slow it down");
            }
            if (! CheckArmMovement(joints))
            {
                isError = true;
                return new KeyValuePair<int, string>(0, "Move only the forearms keeping the rest of the body fixed");
            }
            return new KeyValuePair<int, string>(1, "You are doing good, keep it up");
        }

        private bool CheckArmMovement(JointCollection joints)
        {
            if (!_hasStarted) return true;

            var rightDist = JointsOperations.ComputeEuclideanDistance(joints[JointType.ElbowRight], _startRightElbowPosition);
            var leftDist = JointsOperations.ComputeEuclideanDistance(joints[JointType.ElbowLeft], _startLeftElbowPosition);
            return leftDist < 0.3 && rightDist < 0.3;
        }

    }
}
