using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Bachelor_Client.Utils;
using Microsoft.Kinect;

namespace Bachelor_Client.Pose
{
    public class ShoulderPress : Exercise
    {
        public ShoulderPress(int reps) : base(reps)
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

            return angleLeft <= 100
                   && angleRight <= 100
                   && joints[JointType.WristRight].Position.Y > joints[JointType.ShoulderRight].Position.Y
                   && joints[JointType.WristLeft].Position.Y > joints[JointType.ShoulderLeft].Position.Y;
        }

        public override bool IsEnd(JointCollection joints)
        {
            var angleLeft = JointsOperations.Get2DAngle(joints[JointType.ShoulderLeft],
                joints[JointType.ElbowLeft],
                joints[JointType.WristLeft]);

            var angleRight = JointsOperations.Get2DAngle(joints[JointType.ShoulderRight],
                joints[JointType.ElbowRight],
                joints[JointType.WristRight]);

            return angleLeft >= 160
                   && angleRight >= 160
                   && joints[JointType.WristRight].Position.Y > joints[JointType.ShoulderRight].Position.Y
                   && joints[JointType.WristLeft].Position.Y > joints[JointType.ShoulderLeft].Position.Y;
        }

        public override KeyValuePair<int, string> CheckErrors(JointCollection joints)
        {
            if (!CheckExtension(joints))
            {
                isError = true;
                return new KeyValuePair<int, string>(0, "Try to keep your wrists(hands) right above the elbows");
            }
            return new KeyValuePair<int, string>(1, "You are doing good, keep it up");
        }

        private bool CheckExtension(JointCollection joints)
        {
            return GetDistanceX(joints[JointType.WristRight], joints[JointType.ElbowRight]) < 0.1f
                   && GetDistanceX(joints[JointType.WristLeft], joints[JointType.ElbowLeft]) < 0.1f;
        }
    }
}
