using Bachelor_Client.Entities;
using Microsoft.Kinect;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bachelor_Client.Utils
{
    public class FrameQueue
    {
        int Capacity { get; set; }
        int Size { get; set; }
        Queue<List<SkeletonPoint>> Elements { get; set; }

        public FrameQueue(int capacity = 15)
        {
            Capacity = capacity;
            Size = 0;
        }

        private void Pop()
        {
            Elements.Dequeue();
        }

        public bool Insert(List<SkeletonPoint> elem)
        {
            Elements.Enqueue(elem);
            Size++;
            if (Size > Capacity)
            {
                Pop();
                Size--;
                return true;
            }
            return false;
        }
    }
}
