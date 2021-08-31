using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Bachelor_Client.Entities;
using Bachelor_Client.Pose;
using Bachelor_Client.Utils;
using Microsoft.Kinect;
using Newtonsoft.Json;

namespace Bachelor_Client
{
    public partial class MainPage : Form
    {
        private KinectSensor _kSensor;
        private ExerciseModel _exerciseModel;
        private int _maxReps;
        private int _reps;
        private int _goodReps;
        private Exercise _exercise;
        private bool _hasStarted;
        private Stopwatch _startTime;
        private Stopwatch _fpsTime;
        private int _fps;
        private string _state;
        private MistakesDictionary _mistakesDict;
        

        public MainPage(ExerciseModel model, int reps, Exercise exercise)
        {
            InitializeComponent();
            WindowState = FormWindowState.Normal;
            _exerciseModel = model;
            _maxReps = reps;
            _exercise = exercise;
            nameLabel.Text = "Current exercise: " + _exerciseModel.Name;
            explanationText.Text = "Explanations:\nRelaxation time";
            currentState.Text = "Current state: Wait";
            _hasStarted = false;
            _startTime = new Stopwatch();
            _startTime.Start();
            _fps = 0;
            _state = "";
            _mistakesDict = new MistakesDictionary();
            prevMistakesText.ForeColor = Color.Red;
            StartSensor();
        }

        private string ConvertTime(int seconds)
        {
            var minutes = (int)seconds / 60;
            seconds = seconds % 60;
            var minStr = minutes.ToString();
            var secStr = seconds.ToString();
            if (minutes == 0)
            {
                minStr = "00";
            }
            else if (minutes < 10)
            {
                minStr = "0" + minutes.ToString();
            }
            if (seconds == 0)
            {
                secStr = "00";
            }
            else if (seconds < 10)
            {
                secStr = "0" + seconds.ToString();
            }
            return minStr + ":" + secStr;
        }


        private void StartSet()
        {
            _startTime.Stop();
            _startTime = new Stopwatch();
            actionBtn.Text = "End set";
            explanationText.Text = "Explanations:\nGet in the starting position";
            currentState.Text = "Wait for start";
            stateImage.Image = Image.FromFile(@_exerciseModel.StartPic);
            _hasStarted = true;
            currentRepLabel.Text = "Current repetition is OK";
            currentRepLabel.ForeColor = Color.Green;
            _startTime.Start();
        }


        private void EndSet()
        {
            actionBtn.Text = "Start set";
            explanationText.Text = "Explanations:\nRelaxation time";
            currentState.Text = "Pause";
            stateImage.Image = null;
            _hasStarted = false;
            currentRepLabel.Text = "";
            currentRepLabel.ForeColor = Color.Green;
            currentMistakeText.Text = "";
            prevMistakesText.Text = "";
            _startTime.Stop();
            SummaryForm form = new SummaryForm(_exercise.GetReps(), _exercise.GetGoodReps(), (int)_startTime.Elapsed.TotalSeconds);
            _startTime = new Stopwatch();
            _startTime.Start();
            form.ShowDialog();
        }

        public void StartSensor()
        {
            if (KinectSensor.KinectSensors.Count() > 0)
            {
                _kSensor = KinectSensor.KinectSensors[0];
            }
            _kSensor.Start();
            _kSensor.ColorStream.Enable(ColorImageFormat.RgbResolution640x480Fps30);
            // _kSensor.ColorFrameReady += kSensor_ColorFrameReady;
            _kSensor.DepthStream.Enable();
            _kSensor.DepthStream.Range = DepthRange.Default;
            _kSensor.SkeletonStream.Enable();
            _kSensor.SkeletonStream.TrackingMode = SkeletonTrackingMode.Default;
            _kSensor.AllFramesReady += KSensor_AllFramesReady;
        }

        private void KSensor_AllFramesReady(object sender, AllFramesReadyEventArgs e)
        {
            using (ColorImageFrame VFrame = e.OpenColorImageFrame())
            {
                if (VFrame == null) return;
                byte[] pixelS = new byte[VFrame.PixelDataLength];
                var bmap = CreateBitmapFromSensor(VFrame);
                using (var frame = e.OpenSkeletonFrame())
                {
                    if (frame != null)
                    {
                        var skeletons = new Skeleton[frame.SkeletonArrayLength];
                        frame.CopySkeletonDataTo(skeletons);

                        var trackedSkeleton =
                            skeletons.FirstOrDefault(s => s.TrackingState == SkeletonTrackingState.Tracked);

                        if (trackedSkeleton != null)
                        {
                            Graphics g = Graphics.FromImage(bmap);

                            g = DrawSkeleton(trackedSkeleton, g);

                            if (_hasStarted)
                            {
                                CheckRep(trackedSkeleton.Joints);
                                CheckError(trackedSkeleton.Joints);
                                if (_exercise.IsDone())
                                {
                                    EndSet();
                                }
                            }

                            //var position = trackedSkeleton.Joints[JointType.HandRight].Position;
                        }
                        Update();
                    }
                }
                if (bmap != null)
                {
                    currentImage.Image = bmap;
                }
            }
        }

        private void kSensor_ColorFrameReady(object sender, ColorImageFrameReadyEventArgs e)
        {
            using (var frame = e.OpenColorImageFrame())
            {
                if (frame != null)
                {
                    currentImage.Image = CreateBitmapFromSensor(frame);
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

        Point GetJoint(JointType j, Skeleton S)
        {
            SkeletonPoint Sloc = S.Joints[j].Position;
            ColorImagePoint Cloc =
                _kSensor.MapSkeletonPointToColor(Sloc,
                    ColorImageFormat.RgbResolution640x480Fps30);
            return new Point(Cloc.X, Cloc.Y);
        }

        void DrawBone(JointType j1, JointType j2, Skeleton S, Graphics g)
        {
            Point p1 = GetJoint(j1, S);
            Point p2 = GetJoint(j2, S);
            g.DrawLine(new Pen(Color.Red, 5f), p1, p2);
        }

        Graphics DrawSkeleton(Skeleton S, Graphics g)
        {
            //body
            DrawBone(JointType.Head, JointType.ShoulderCenter, S, g);
            DrawBone(JointType.ShoulderCenter, JointType.Spine, S, g);
            DrawBone(JointType.Spine, JointType.HipCenter, S, g);
            //left leg
            DrawBone(JointType.HipCenter, JointType.HipLeft, S, g);
            DrawBone(JointType.HipLeft, JointType.KneeLeft, S, g);
            DrawBone(JointType.KneeLeft, JointType.AnkleLeft, S, g);
            DrawBone(JointType.AnkleLeft, JointType.FootLeft, S, g);
            //Right Leg
            DrawBone(JointType.HipCenter, JointType.HipRight, S, g);
            DrawBone(JointType.HipRight, JointType.KneeRight, S, g);
            DrawBone(JointType.KneeRight, JointType.AnkleRight, S, g);
            DrawBone(JointType.AnkleRight, JointType.FootRight, S, g);
            //Left Arm
            DrawBone(JointType.ShoulderCenter, JointType.ShoulderLeft, S, g);
            DrawBone(JointType.ShoulderLeft, JointType.ElbowLeft, S, g);
            DrawBone(JointType.ElbowLeft, JointType.WristLeft, S, g);
            DrawBone(JointType.WristLeft, JointType.HandLeft, S, g);
            //Right Arm
            DrawBone(JointType.ShoulderCenter, JointType.ShoulderRight, S, g);
            DrawBone(JointType.ShoulderRight, JointType.ElbowRight, S, g);
            DrawBone(JointType.ElbowRight, JointType.WristRight, S, g);
            DrawBone(JointType.WristRight, JointType.HandRight, S, g);

            return g;
        }

        private void actionBtn_Click(object sender, EventArgs e)
        {

            if (actionBtn.Text == "Start set")
            {
                StartSet();
            }
            else
            {
                EndSet();
            }
        }

        private void Update()
        {
            var elapse = (int)_startTime.Elapsed.TotalSeconds;
            timeLabel.Text = "Time elapsed: " + ConvertTime(elapse);
        }

        private void CheckRep(JointCollection joints)
        {
            KeyValuePair<string, int> pair = _exercise.CheckRepetition(joints);
            CheckState(pair.Key);
        }

        private void CheckState(string state)
        {
            if (_state == "" && state == "start")
            {
                _state = "start";
                explanationText.Text = "Explanations:\n" + _exerciseModel.RepsExplanationsDict[state];
                currentState.Text = "Current state: Start";
                stateImage.Image = Image.FromFile(@_exerciseModel.EndPic);
                currentRepLabel.Text = "Current repetition is OK";
                currentRepLabel.ForeColor = Color.Green;
            }
            if (_state == "start" && state == "end")
            {
                _state = "end";
                explanationText.Text = "Explanations:\n" + _exerciseModel.RepsExplanationsDict[state];
                currentState.Text = "Current state: End";
                stateImage.Image = Image.FromFile(@_exerciseModel.StartPic);
            }
            if (_state == "end" && state == "start")
            {
                _state = "start";
                explanationText.Text = "Explanations:\n" + _exerciseModel.RepsExplanationsDict[state];
                currentState.Text = "Current state: Start";
                stateImage.Image = Image.FromFile(@_exerciseModel.EndPic);
                currentRepLabel.Text = "Current repetition is OK";
                currentRepLabel.ForeColor = Color.Green;
                _reps += 1;
                repsLabel.Text = "Number of reps: " + _reps.ToString();
            }
        }

        private void CheckError(JointCollection joints)
        {
            KeyValuePair<int, string> pair = _exercise.CheckErrors(joints);
            if (pair.Key == 0)
            {
                currentMistakeText.Text = pair.Value;
                currentMistakeText.ForeColor = Color.Red;
                currentRepLabel.Text = "Current repetition is bad";
                currentRepLabel.ForeColor = Color.Red;
                _mistakesDict.AddMistake(_reps + 1, pair.Value);
                SetMistakesText();
            }
            if (pair.Key == 1)
            {
                currentMistakeText.Text = pair.Value;
                currentMistakeText.ForeColor = Color.Green;
            }
        }

        private void SetMistakesText()
        {
            StringBuilder str = new StringBuilder();
            foreach (var mist in _mistakesDict.Mistakes)
                str.AppendLine("Rep " + mist.Key + ": " + mist.Value);
            prevMistakesText.Text = str.ToString();
            str.Clear();
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void MainPage_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (MessageBox.Show("Do you want to save the current activity?", "Exit",
                MessageBoxButtons.YesNo) == DialogResult.Yes)
            {
                var json = JsonConvert.SerializeObject(ActivityManager.GetActivity());
                File.WriteAllText(@"activity.json", json);
                //write to file
            }
        }
    }
}
