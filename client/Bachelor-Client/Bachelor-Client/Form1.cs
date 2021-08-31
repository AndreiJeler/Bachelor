using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using Microsoft.Kinect;

namespace Bachelor_Client
{
    public partial class Form1 : Form
    {
        private KinectSensor kSensor;

        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {
           
        }

        private void KinectSensors_StatusChanged(object sender, StatusChangedEventArgs e)
        {
            this.lblStatus.Text = kSensor.Status.ToString();
        }

        private void btnStream_Click(object sender, EventArgs e)
        {
            if (btnStream.Text == "Stream")
            {
                if (KinectSensor.KinectSensors.Count() > 0)
                {
                    btnStream.Text = "Stop stream";
                    kSensor = KinectSensor.KinectSensors[0];
                    KinectSensor.KinectSensors.StatusChanged += KinectSensors_StatusChanged;
                }
                kSensor.Start();
                this.lblID.Text = kSensor.DeviceConnectionId;
                kSensor.ColorStream.Enable(ColorImageFormat.RgbResolution640x480Fps30);
                kSensor.ColorFrameReady += kSensor_ColorFrameReady;
                kSensor.DepthStream.Enable();
                kSensor.DepthStream.Range = DepthRange.Default;
                kSensor.AllFramesReady += KSensor_AllFramesReady;
                kSensor.SkeletonStream.Enable();
                kSensor.SkeletonStream.TrackingMode = SkeletonTrackingMode.Default;
            }
            else
            {
                if (kSensor != null && kSensor.IsRunning)
                {
                    kSensor.Stop();
                    this.btnStream.Text = "Stream";
                    this.pbStream.Image = null;
                }
            }
        }

        private void KSensor_AllFramesReady(object sender, AllFramesReadyEventArgs e)
        {
            using (var frame = e.OpenSkeletonFrame())
            {
                if (frame == null)
                {
                    return;
                    //pbStream.Image = CreateBitmapFromSensor(frame);
                }
                var skeletons = new Skeleton[frame.SkeletonArrayLength];
                frame.CopySkeletonDataTo(skeletons);

                var trackedSkeleton = skeletons.FirstOrDefault(s => s.TrackingState == SkeletonTrackingState.Tracked);

                if (trackedSkeleton == null) return;

                var position = trackedSkeleton.Joints[JointType.HandRight].Position;
            }
        }

        private void kSensor_ColorFrameReady(object sender, ColorImageFrameReadyEventArgs e)
        {
            using(var frame = e.OpenColorImageFrame())
            {
                if (frame != null)
                {
                    pbStream.Image = CreateBitmapFromSensor(frame);
                }
            }
        }

        private Bitmap CreateBitmapFromSensor(ColorImageFrame frame)
        {
            var pixelData = new byte[frame.PixelDataLength];
            frame.CopyPixelDataTo(pixelData);

            //return pixelData.ToBitmap(frame.Width, frame.Height);

            var stride = frame.Width * frame.BytesPerPixel;

            var bmpFrame = new Bitmap(frame.Width, frame.Height, System.Drawing.Imaging.PixelFormat.Format32bppRgb);
            var bmpData = bmpFrame.LockBits(new Rectangle(0, 0, frame.Width, frame.Height), System.Drawing.Imaging.ImageLockMode.WriteOnly, bmpFrame.PixelFormat);

            System.Runtime.InteropServices.Marshal.Copy(pixelData, 0, bmpData.Scan0, frame.PixelDataLength);

            bmpFrame.UnlockBits(bmpData);
            return bmpFrame;
        }
    }
}
