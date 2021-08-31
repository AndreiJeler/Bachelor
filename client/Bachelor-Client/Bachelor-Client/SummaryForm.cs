using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Bachelor_Client.Entities;
using Bachelor_Client.Utils;

namespace Bachelor_Client
{
    public partial class SummaryForm : Form
    {
        private int _reps;
        private int _goodReps;
        private int _seconds;

        public SummaryForm(int reps, int goodReps, int seconds)
        {
            InitializeComponent();

            _reps = reps;
            _goodReps = goodReps;
            _seconds = seconds;

            secondsLabel.Text = seconds.ToString();
            repsLabel.Text = reps.ToString();
            goodRepsLabel.Text = goodReps.ToString();
        }

        private void saveBtn_Click(object sender, EventArgs e)
        {
            var details = detailsText.Text;
            var set = new Set { nr_reps = _reps, good_reps = _goodReps, seconds = _seconds, details = details };
            ActivityManager.AddSet(set);
            Close();
        }
    }
}
