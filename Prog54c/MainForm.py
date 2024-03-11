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
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.HotPink
		self._label1.Location = System.Drawing.Point(42, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(216, 42)
		self._label1.TabIndex = 0
		self._label1.Text = "Radius: "
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.HotPink
		self._label2.Location = System.Drawing.Point(295, 142)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(216, 42)
		self._label2.TabIndex = 1
		self._label2.Text = "Area: "
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.HotPink
		self._label3.Location = System.Drawing.Point(42, 142)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(216, 42)
		self._label3.TabIndex = 2
		self._label3.Text = "Circumference: "
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Gainsboro
		self._textBox1.Location = System.Drawing.Point(275, 27)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(208, 20)
		self._textBox1.TabIndex = 3
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Sienna
		self._button1.Location = System.Drawing.Point(42, 195)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(216, 80)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Sienna
		self._button2.Location = System.Drawing.Point(295, 195)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(216, 80)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(609, 290)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		rad = int(self._textBox1.Text)
		pi = 3.14159
		cir = 2 * pi * rad
		are = pi * rad * rad
		self._label2.Text = "Circumference: " + cir
		self._label3.Text = "Area: " + are

	def Button2Click(self, sender, e):
		self._label2.Text = "Circumference "
		self._label3.Text = "Area: "
		self._textBox1.Text = ""