import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.PaleTurquoise
		self._label1.Location = System.Drawing.Point(7, 16)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(195, 42)
		self._label1.TabIndex = 0
		self._label1.Text = "Speed Limit:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.PaleTurquoise
		self._label2.Location = System.Drawing.Point(7, 99)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(195, 42)
		self._label2.TabIndex = 1
		self._label2.Text = "Vehicle Speed:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(210, 28)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(191, 20)
		self._textBox1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(210, 111)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(191, 20)
		self._textBox2.TabIndex = 3
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Aquamarine
		self._button1.Location = System.Drawing.Point(0, 226)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(127, 78)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Aquamarine
		self._button2.Location = System.Drawing.Point(164, 226)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(127, 78)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Aquamarine
		self._button3.Location = System.Drawing.Point(330, 226)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(127, 78)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Lime
		self._label3.Location = System.Drawing.Point(164, 159)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(126, 45)
		self._label3.TabIndex = 7
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MediumTurquoise
		self.ClientSize = System.Drawing.Size(481, 305)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog82a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		limit = int(self._textBox1.Text)
		speed = int(self._textBox2.Text)
		fine = 20 + speed > limit * 5
		self._label3.Text = "Result: " + fine
		
