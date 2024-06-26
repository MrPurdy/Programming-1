﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.PeachPuff
		self._label1.Location = System.Drawing.Point(39, 36)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(201, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter the number of calories in the food:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Cornsilk
		self._textBox1.Location = System.Drawing.Point(270, 39)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Cornsilk
		self._textBox2.Location = System.Drawing.Point(270, 108)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 3
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.PeachPuff
		self._label2.Location = System.Drawing.Point(39, 105)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(201, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Enter the number of fat grams in the food"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.PeachPuff
		self._label3.Location = System.Drawing.Point(39, 172)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(201, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Percentage of calories that come from fat"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.PeachPuff
		self._label4.Location = System.Drawing.Point(270, 172)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 5
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Peru
		self._button1.Location = System.Drawing.Point(32, 230)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(104, 73)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Peru
		self._button2.Location = System.Drawing.Point(165, 230)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(104, 73)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Peru
		self._button3.Location = System.Drawing.Point(294, 230)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(104, 73)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightSalmon
		self.ClientSize = System.Drawing.Size(452, 311)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg268FatCalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		cal = int(self._textBox1.Text)
		grams = int(self._textBox2.Text)
		calsfromfat = grams * 9
		percentagefat = calsfromfat / cal
		self._label4.Text = str(percentagefat)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()