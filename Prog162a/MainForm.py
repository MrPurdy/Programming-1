import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.PaleGoldenrod
		self._button1.Location = System.Drawing.Point(5, 321)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(158, 98)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.PaleGoldenrod
		self._button2.Location = System.Drawing.Point(199, 321)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(158, 98)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.PaleGoldenrod
		self._button3.Location = System.Drawing.Point(399, 321)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(158, 98)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Chocolate
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 11, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(35, 26)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(239, 75)
		self._label1.TabIndex = 5
		self._label1.Text = "Enter a number between 1-12"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Chocolate
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 11, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(35, 127)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(500, 143)
		self._label2.TabIndex = 6
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.MediumSeaGreen
		self._textBox1.Location = System.Drawing.Point(292, 53)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(206, 20)
		self._textBox1.TabIndex = 7
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.YellowGreen
		self.ClientSize = System.Drawing.Size(569, 427)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog162a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		for num in range(1, 12+1):
			num = int(self._textBox1.Text)
			numf = math.factorial(num)
			self._label2.Text = "The value of " + str(num) + "! is " + str(numf)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()