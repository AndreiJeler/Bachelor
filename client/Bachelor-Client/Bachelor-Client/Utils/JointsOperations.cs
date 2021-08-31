using Bachelor_Client.Pose;
using Microsoft.Kinect;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Bachelor_Client.Utils
{
    public static class JointsOperations
    {
        public static double Get2DAngle(Joint jointA, Joint jointB, Joint jointC)
        {
            Entities.Joint j1 = new Entities.Joint(jointA.Position.X, jointA.Position.Y, jointA.Position.Z);
            Entities.Joint j2 = new Entities.Joint(jointB.Position.X, jointB.Position.Y, jointB.Position.Z);
            Entities.Joint j3 = new Entities.Joint(jointC.Position.X, jointC.Position.Y, jointC.Position.Z);

            Entities.Joint v1 = j1 - j3;
            Entities.Joint v2 = j1 - j2;

            var angle = Math.Atan2(j3.Y - j2.Y, j3.X - j2.X) - Math.Atan2(j1.Y - j2.Y, j1.X - j2.X);
            angle = Math.Abs(angle * 180.0d / Math.PI);

            if (angle > 180)
            {
                angle = 360 - angle;
            }

            return angle;
        }

        public static double ComputeEuclideanDistance(Joint jA, Joint jB)
        {
            return Math.Sqrt(Math.Pow(jA.Position.X - jB.Position.X, 2) + Math.Pow(jA.Position.Y - jB.Position.Y, 2) +
                             Math.Pow(jA.Position.Z - jB.Position.Z, 2));
        }

        public static Exercise CreateExerciseClass(string exerciseName, int maxReps) {
            switch (exerciseName)
            {
                case "Squats":
                    return new Squats(maxReps);
                case "Shoulder press":
                    return new ShoulderPress(maxReps);
                default:
                    return new BicepCurl(maxReps);
            }
        }
    }
}
