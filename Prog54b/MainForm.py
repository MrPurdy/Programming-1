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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DodgerBlue
		self._label1.Location = System.Drawing.Point(8, 17)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(172, 35)
		self._label1.TabIndex = 0
		self._label1.Text = "Number 1:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DodgerBlue
		self._label2.Location = System.Drawing.Point(8, 64)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(172, 35)
		self._label2.TabIndex = 1
		self._label2.Text = "Number 1:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DodgerBlue
		self._label3.Location = System.Drawing.Point(8, 110)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(172, 35)
		self._label3.TabIndex = 2
		self._label3.Text = "Number 1:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DodgerBlue
		self._label4.Location = System.Drawing.Point(8, 158)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(172, 35)
		self._label4.TabIndex = 3
		self._label4.Text = "Number 1:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(189, 25)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(187, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.White
		self._textBox2.Location = System.Drawing.Point(189, 72)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(187, 20)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.White
		self._textBox3.Location = System.Drawing.Point(189, 118)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(187, 20)
		self._textBox3.TabIndex = 6
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.Color.White
		self._textBox4.Location = System.Drawing.Point(189, 166)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(187, 20)
		self._textBox4.TabIndex = 7
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightCoral
		self._label5.Location = System.Drawing.Point(18, 208)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(162, 26)
		self._label5.TabIndex = 8
		self._label5.Text = "Sum:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightCoral
		self._label6.Location = System.Drawing.Point(18, 253)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(162, 26)
		self._label6.TabIndex = 9
		self._label6.Text = "Average:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(226, 209)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(127, 69)
		self._button1.TabIndex = 10
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(378, 209)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(121, 69)
		self._button2.TabIndex = 11
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(511, 305)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog54b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox1.Text)
		num3 = int(self._textBox1.Text)
		num4 = int(self._textBox1.Text)
		sum = num1 + num2 + num3 + num4
		average = sum / 4
		self.label5.Text = "Sum: " + sum
		self.label6.Text = "Average: " + average

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self.label5.Text = "Sum:"
		self.label6.Text = "Average:"