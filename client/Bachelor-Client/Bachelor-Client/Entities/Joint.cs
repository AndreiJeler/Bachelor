using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bachelor_Client.Entities
{
    public class Joint
    {
        public float X { get; set; }
        public float Y { get; set; }
        public float Z { get; set; }

        public Joint(float x, float y, float z)
        {
            X = x;
            Y = y;
            Z = z;
        }

        public static Joint operator -(Joint joint1, Joint joint2)
        {
            return new Joint(joint1.X - joint2.X, joint1.Y - joint2.Y, joint1.Z - joint2.Z);
        }

    }
}
