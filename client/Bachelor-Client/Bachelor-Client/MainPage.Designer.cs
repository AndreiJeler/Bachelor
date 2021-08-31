
namespace Bachelor_Client
{
    partial class MainPage
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.tableLayoutPanel1 = new System.Windows.Forms.TableLayoutPanel();
            this.tableLayoutPanel2 = new System.Windows.Forms.TableLayoutPanel();
            this.currentImage = new System.Windows.Forms.PictureBox();
            this.nameLabel = new System.Windows.Forms.Label();
            this.tableLayoutPanel3 = new System.Windows.Forms.TableLayoutPanel();
            this.currentState = new System.Windows.Forms.Label();
            this.stateImage = new System.Windows.Forms.PictureBox();
            this.explanationText = new System.Windows.Forms.Label();
            this.tableLayoutPanel4 = new System.Windows.Forms.TableLayoutPanel();
            this.label1 = new System.Windows.Forms.Label();
            this.actionBtn = new System.Windows.Forms.Button();
            this.repsLabel = new System.Windows.Forms.Label();
            this.timeLabel = new System.Windows.Forms.Label();
            this.summaryPanel = new System.Windows.Forms.Panel();
            this.prevMistakesText = new System.Windows.Forms.RichTextBox();
            this.currentMistakeText = new System.Windows.Forms.RichTextBox();
            this.currentRepLabel = new System.Windows.Forms.Label();
            this.tableLayoutPanel1.SuspendLayout();
            this.tableLayoutPanel2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.currentImage)).BeginInit();
            this.tableLayoutPanel3.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.stateImage)).BeginInit();
            this.tableLayoutPanel4.SuspendLayout();
            this.summaryPanel.SuspendLayout();
            this.SuspendLayout();
            // 
            // tableLayoutPanel1
            // 
            this.tableLayoutPanel1.CellBorderStyle = System.Windows.Forms.TableLayoutPanelCellBorderStyle.Single;
            this.tableLayoutPanel1.ColumnCount = 3;
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 60F));
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 20F));
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 20F));
            this.tableLayoutPanel1.Controls.Add(this.tableLayoutPanel2, 0, 0);
            this.tableLayoutPanel1.Controls.Add(this.tableLayoutPanel3, 1, 0);
            this.tableLayoutPanel1.Controls.Add(this.tableLayoutPanel4, 2, 0);
            this.tableLayoutPanel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tableLayoutPanel1.Location = new System.Drawing.Point(0, 0);
            this.tableLayoutPanel1.Margin = new System.Windows.Forms.Padding(0);
            this.tableLayoutPanel1.Name = "tableLayoutPanel1";
            this.tableLayoutPanel1.RowCount = 1;
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 10F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 90F));
            this.tableLayoutPanel1.Size = new System.Drawing.Size(1264, 681);
            this.tableLayoutPanel1.TabIndex = 0;
            // 
            // tableLayoutPanel2
            // 
            this.tableLayoutPanel2.ColumnCount = 1;
            this.tableLayoutPanel2.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.tableLayoutPanel2.Controls.Add(this.currentImage, 0, 1);
            this.tableLayoutPanel2.Controls.Add(this.nameLabel, 0, 0);
            this.tableLayoutPanel2.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tableLayoutPanel2.Location = new System.Drawing.Point(1, 1);
            this.tableLayoutPanel2.Margin = new System.Windows.Forms.Padding(0);
            this.tableLayoutPanel2.Name = "tableLayoutPanel2";
            this.tableLayoutPanel2.RowCount = 2;
            this.tableLayoutPanel2.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 8F));
            this.tableLayoutPanel2.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 92F));
            this.tableLayoutPanel2.Size = new System.Drawing.Size(756, 679);
            this.tableLayoutPanel2.TabIndex = 0;
            // 
            // currentImage
            // 
            this.currentImage.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(57)))), ((int)(((byte)(62)))), ((int)(((byte)(70)))));
            this.currentImage.Dock = System.Windows.Forms.DockStyle.Fill;
            this.currentImage.Location = new System.Drawing.Point(0, 54);
            this.currentImage.Margin = new System.Windows.Forms.Padding(0);
            this.currentImage.Name = "currentImage";
            this.currentImage.Size = new System.Drawing.Size(756, 625);
            this.currentImage.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.currentImage.TabIndex = 0;
            this.currentImage.TabStop = false;
            // 
            // nameLabel
            // 
            this.nameLabel.AutoSize = true;
            this.nameLabel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.nameLabel.Location = new System.Drawing.Point(0, 0);
            this.nameLabel.Margin = new System.Windows.Forms.Padding(0);
            this.nameLabel.Name = "nameLabel";
            this.nameLabel.Size = new System.Drawing.Size(756, 54);
            this.nameLabel.TabIndex = 1;
            this.nameLabel.Text = "Current exercise: Squats";
            this.nameLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // tableLayoutPanel3
            // 
            this.tableLayoutPanel3.ColumnCount = 1;
            this.tableLayoutPanel3.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.tableLayoutPanel3.Controls.Add(this.currentState, 0, 0);
            this.tableLayoutPanel3.Controls.Add(this.stateImage, 0, 1);
            this.tableLayoutPanel3.Controls.Add(this.explanationText, 0, 2);
            this.tableLayoutPanel3.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tableLayoutPanel3.Location = new System.Drawing.Point(758, 1);
            this.tableLayoutPanel3.Margin = new System.Windows.Forms.Padding(0);
            this.tableLayoutPanel3.Name = "tableLayoutPanel3";
            this.tableLayoutPanel3.RowCount = 3;
            this.tableLayoutPanel3.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 8F));
            this.tableLayoutPanel3.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 60F));
            this.tableLayoutPanel3.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 32F));
            this.tableLayoutPanel3.Size = new System.Drawing.Size(252, 679);
            this.tableLayoutPanel3.TabIndex = 1;
            // 
            // currentState
            // 
            this.currentState.AutoSize = true;
            this.currentState.Dock = System.Windows.Forms.DockStyle.Fill;
            this.currentState.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.currentState.Location = new System.Drawing.Point(0, 0);
            this.currentState.Margin = new System.Windows.Forms.Padding(0);
            this.currentState.Name = "currentState";
            this.currentState.Size = new System.Drawing.Size(252, 54);
            this.currentState.TabIndex = 0;
            this.currentState.Text = "Current state: Start";
            this.currentState.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // stateImage
            // 
            this.stateImage.Dock = System.Windows.Forms.DockStyle.Fill;
            this.stateImage.Location = new System.Drawing.Point(0, 54);
            this.stateImage.Margin = new System.Windows.Forms.Padding(0);
            this.stateImage.Name = "stateImage";
            this.stateImage.Size = new System.Drawing.Size(252, 407);
            this.stateImage.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.stateImage.TabIndex = 1;
            this.stateImage.TabStop = false;
            // 
            // explanationText
            // 
            this.explanationText.AutoSize = true;
            this.explanationText.Dock = System.Windows.Forms.DockStyle.Fill;
            this.explanationText.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.explanationText.Location = new System.Drawing.Point(3, 461);
            this.explanationText.Name = "explanationText";
            this.explanationText.Size = new System.Drawing.Size(246, 218);
            this.explanationText.TabIndex = 2;
            this.explanationText.Text = "Explanations:";
            // 
            // tableLayoutPanel4
            // 
            this.tableLayoutPanel4.ColumnCount = 1;
            this.tableLayoutPanel4.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.tableLayoutPanel4.Controls.Add(this.label1, 0, 2);
            this.tableLayoutPanel4.Controls.Add(this.actionBtn, 0, 4);
            this.tableLayoutPanel4.Controls.Add(this.repsLabel, 0, 0);
            this.tableLayoutPanel4.Controls.Add(this.timeLabel, 0, 1);
            this.tableLayoutPanel4.Controls.Add(this.summaryPanel, 0, 3);
            this.tableLayoutPanel4.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tableLayoutPanel4.Location = new System.Drawing.Point(1011, 1);
            this.tableLayoutPanel4.Margin = new System.Windows.Forms.Padding(0);
            this.tableLayoutPanel4.Name = "tableLayoutPanel4";
            this.tableLayoutPanel4.RowCount = 5;
            this.tableLayoutPanel4.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 8F));
            this.tableLayoutPanel4.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 8F));
            this.tableLayoutPanel4.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 6F));
            this.tableLayoutPanel4.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 65F));
            this.tableLayoutPanel4.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 13F));
            this.tableLayoutPanel4.Size = new System.Drawing.Size(252, 679);
            this.tableLayoutPanel4.TabIndex = 2;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.label1.Location = new System.Drawing.Point(0, 108);
            this.label1.Margin = new System.Windows.Forms.Padding(0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(252, 40);
            this.label1.TabIndex = 0;
            this.label1.Text = "Summary:";
            // 
            // actionBtn
            // 
            this.actionBtn.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(34)))), ((int)(((byte)(40)))), ((int)(((byte)(49)))));
            this.actionBtn.Dock = System.Windows.Forms.DockStyle.Fill;
            this.actionBtn.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.actionBtn.Location = new System.Drawing.Point(0, 589);
            this.actionBtn.Margin = new System.Windows.Forms.Padding(0);
            this.actionBtn.Name = "actionBtn";
            this.actionBtn.Size = new System.Drawing.Size(252, 90);
            this.actionBtn.TabIndex = 1;
            this.actionBtn.Text = "Start set";
            this.actionBtn.UseVisualStyleBackColor = false;
            this.actionBtn.Click += new System.EventHandler(this.actionBtn_Click);
            // 
            // repsLabel
            // 
            this.repsLabel.AutoSize = true;
            this.repsLabel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.repsLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.repsLabel.Location = new System.Drawing.Point(3, 0);
            this.repsLabel.Name = "repsLabel";
            this.repsLabel.Size = new System.Drawing.Size(246, 54);
            this.repsLabel.TabIndex = 2;
            this.repsLabel.Text = "Number of reps: 0";
            this.repsLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // timeLabel
            // 
            this.timeLabel.AutoSize = true;
            this.timeLabel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.timeLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.timeLabel.Location = new System.Drawing.Point(3, 54);
            this.timeLabel.Name = "timeLabel";
            this.timeLabel.Size = new System.Drawing.Size(246, 54);
            this.timeLabel.TabIndex = 3;
            this.timeLabel.Text = "Time Elapsed: 00:00";
            this.timeLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // summaryPanel
            // 
            this.summaryPanel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.summaryPanel.Controls.Add(this.prevMistakesText);
            this.summaryPanel.Controls.Add(this.currentMistakeText);
            this.summaryPanel.Controls.Add(this.currentRepLabel);
            this.summaryPanel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.summaryPanel.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.summaryPanel.Location = new System.Drawing.Point(0, 148);
            this.summaryPanel.Margin = new System.Windows.Forms.Padding(0);
            this.summaryPanel.Name = "summaryPanel";
            this.summaryPanel.Size = new System.Drawing.Size(252, 441);
            this.summaryPanel.TabIndex = 4;
            // 
            // prevMistakesText
            // 
            this.prevMistakesText.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(57)))), ((int)(((byte)(62)))), ((int)(((byte)(70)))));
            this.prevMistakesText.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.prevMistakesText.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.prevMistakesText.Location = new System.Drawing.Point(0, 178);
            this.prevMistakesText.Name = "prevMistakesText";
            this.prevMistakesText.Size = new System.Drawing.Size(249, 256);
            this.prevMistakesText.TabIndex = 2;
            this.prevMistakesText.Text = "";
            // 
            // currentMistakeText
            // 
            this.currentMistakeText.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(57)))), ((int)(((byte)(62)))), ((int)(((byte)(70)))));
            this.currentMistakeText.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.currentMistakeText.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.currentMistakeText.Location = new System.Drawing.Point(-3, 60);
            this.currentMistakeText.Name = "currentMistakeText";
            this.currentMistakeText.Size = new System.Drawing.Size(249, 98);
            this.currentMistakeText.TabIndex = 1;
            this.currentMistakeText.Text = "";
            this.currentMistakeText.TextChanged += new System.EventHandler(this.richTextBox1_TextChanged);
            // 
            // currentRepLabel
            // 
            this.currentRepLabel.AutoSize = true;
            this.currentRepLabel.ForeColor = System.Drawing.Color.Green;
            this.currentRepLabel.Location = new System.Drawing.Point(3, 12);
            this.currentRepLabel.Name = "currentRepLabel";
            this.currentRepLabel.Size = new System.Drawing.Size(0, 25);
            this.currentRepLabel.TabIndex = 0;
            // 
            // MainPage
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(57)))), ((int)(((byte)(62)))), ((int)(((byte)(70)))));
            this.ClientSize = new System.Drawing.Size(1264, 681);
            this.Controls.Add(this.tableLayoutPanel1);
            this.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(238)))), ((int)(((byte)(238)))), ((int)(((byte)(238)))));
            this.MinimumSize = new System.Drawing.Size(1280, 720);
            this.Name = "MainPage";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Exercise";
            this.WindowState = System.Windows.Forms.FormWindowState.Maximized;
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.MainPage_FormClosing);
            this.tableLayoutPanel1.ResumeLayout(false);
            this.tableLayoutPanel2.ResumeLayout(false);
            this.tableLayoutPanel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.currentImage)).EndInit();
            this.tableLayoutPanel3.ResumeLayout(false);
            this.tableLayoutPanel3.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.stateImage)).EndInit();
            this.tableLayoutPanel4.ResumeLayout(false);
            this.tableLayoutPanel4.PerformLayout();
            this.summaryPanel.ResumeLayout(false);
            this.summaryPanel.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TableLayoutPanel tableLayoutPanel1;
        private System.Windows.Forms.TableLayoutPanel tableLayoutPanel2;
        private System.Windows.Forms.PictureBox currentImage;
        private System.Windows.Forms.Label nameLabel;
        private System.Windows.Forms.TableLayoutPanel tableLayoutPanel3;
        private System.Windows.Forms.Label currentState;
        private System.Windows.Forms.PictureBox stateImage;
        private System.Windows.Forms.TableLayoutPanel tableLayoutPanel4;
        private System.Windows.Forms.Label explanationText;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button actionBtn;
        private System.Windows.Forms.Label repsLabel;
        private System.Windows.Forms.Label timeLabel;
        private System.Windows.Forms.Panel summaryPanel;
        private System.Windows.Forms.RichTextBox currentMistakeText;
        private System.Windows.Forms.Label currentRepLabel;
        private System.Windows.Forms.RichTextBox prevMistakesText;
    }
}