import math
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
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.BurlyWood
		self._label1.Location = System.Drawing.Point(11, 18)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(176, 38)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter A:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.BurlyWood
		self._label2.Location = System.Drawing.Point(11, 132)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(176, 38)
		self._label2.TabIndex = 1
		self._label2.Text = "Enter C:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.BurlyWood
		self._label3.Location = System.Drawing.Point(11, 77)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(176, 38)
		self._label3.TabIndex = 2
		self._label3.Text = "Enter B:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.SeaGreen
		self._label4.Location = System.Drawing.Point(11, 219)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(176, 38)
		self._label4.TabIndex = 3
		self._label4.Text = "The roots are: "
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.MediumPurple
		self._button1.Location = System.Drawing.Point(217, 191)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(117, 94)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.MediumPurple
		self._button2.Location = System.Drawing.Point(351, 191)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(117, 94)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(193, 28)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(201, 20)
		self._textBox1.TabIndex = 6
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(193, 87)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(201, 20)
		self._textBox2.TabIndex = 7
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(193, 142)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(201, 20)
		self._textBox3.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkSlateBlue
		self.ClientSize = System.Drawing.Size(480, 289)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog58b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		a = float(self._textBox1.Text)
		b = float(self._textBox2.Text)
		c = float(self._textBox3.Text)
		positive = (-b + math.sqrt)(b**2 -4*a*c)/(2*a)
		negative = (-b - math.sqrt)(b**2 -4*a*c)/(2*a)
		
		self._label4.Text = "The Roots are: " + str(positive) + str(negative)

	def Button2Click(self, sender, e):
		self._label4.Text = ""