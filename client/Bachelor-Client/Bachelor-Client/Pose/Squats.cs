using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Bachelor_Client.Utils;
using Microsoft.Kinect;

namespace Bachelor_Client.Pose
{
    public class Squats : Exercise
    {
        private Joint _startLeftShoulderPosition;
        private Joint _startRightShoulderPosition;
        private bool _hasStarted;
        public Squats(int reps) : base(reps)
        {
        }

        public override bool IsStart(JointCollection joints)
        {
            var angleLeft = JointsOperations.Get2DAngle(joints[JointType.HipLeft],
                joints[JointType.KneeLeft],
                joints[JointType.FootLeft]);

            var angleRight = JointsOperations.Get2DAngle(joints[JointType.HipRight],
                joints[JointType.KneeRight],
                joints[JointType.FootRight]);

            if (angleLeft >= 165 && angleRight >= 165)
            {
                _startRightShoulderPosition = joints[JointType.ShoulderRight];
                _startLeftShoulderPosition = joints[JointType.ShoulderLeft];
                _hasStarted = true;
                return true;
            }
            return false;
        }

        public override bool IsEnd(JointCollection joints)
        {
            var angleLeft = JointsOperations.Get2DAngle(joints[JointType.HipLeft],
                joints[JointType.KneeLeft],
                joints[JointType.FootLeft]);

            var angleRight = JointsOperations.Get2DAngle(joints[JointType.HipRight],
                joints[JointType.KneeRight],
                joints[JointType.FootRight]);

            return angleLeft <= 110
                   && angleRight <= 110
                   && GetDistanceY(joints[JointType.HipLeft], joints[JointType.KneeLeft]) <= 0.1
                   && GetDistanceY(joints[JointType.HipRight], joints[JointType.HipLeft]) <= 0.1;
        }

        public override KeyValuePair<int, string> CheckErrors(JointCollection joints)
        {
            if (!CheckKneeCave(joints))
            {
                isError = true;
                return new KeyValuePair<int, string>(0, "Try to keep your back straight, do not get the knees close or raise the feet up");
            }
            if (!CheckBackArch(joints))
            {
                isError = true;
                return new KeyValuePair<int, string>(0, "Try to keep your back straight, do not bend it");
            }
            return new KeyValuePair<int, string>(1, "You are doing good, keep it up");
        }

        private bool CheckKneeCave(JointCollection joints)
        {
            return JointsOperations.ComputeEuclideanDistance(joints[JointType.KneeLeft], joints[JointType.KneeRight]) >
                   0.1;
        }

        private bool CheckBackArch(JointCollection joints)
        {
            if (!_hasStarted) return true;

            var rightDist = JointsOperations.ComputeEuclideanDistance(joints[JointType.ShoulderRight], _startRightShoulderPosition);
            var leftDist = JointsOperations.ComputeEuclideanDistance(joints[JointType.ShoulderLeft], _startLeftShoulderPosition);
            return leftDist < 0.25 && rightDist < 0.25;
        }
    }
}
