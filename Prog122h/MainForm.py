import System.Drawing
import System.Windows.Forms
import math

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Lavender
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(13, 8)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(594, 277)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightPink
		self._button1.Location = System.Drawing.Point(18, 302)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(152, 87)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightPink
		self._button2.Location = System.Drawing.Point(229, 302)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(152, 87)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightPink
		self._button3.Location = System.Drawing.Point(441, 302)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(152, 87)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LavenderBlush
		self.ClientSize = System.Drawing.Size(622, 393)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog122h"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Number\t\tSquare\t\tSquare Root\t\tCube\t\t4th Root"
		self._listBox1.Items.Add(heading)
		for num in range(1, 20+1):
			nsqrd = num**2
			nsqrt = math.sqrt(num)
			ncube = num**3
			nftrt = num**(1.0/4.0)
			msg = str(num) + "\t\t" + str(nsqrd) + "\t\t" + str(round(nsqrt, 4)) + "\t\t\t" + str(ncube) + "\t\t" + str(nftrt)
			self._listBox1.Items.Add(msg)
	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()