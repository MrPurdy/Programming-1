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
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightGreen
		self._label1.Location = System.Drawing.Point(13, 14)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(201, 34)
		self._label1.TabIndex = 0
		self._label1.Text = "Pounds: "
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightGreen
		self._label2.Location = System.Drawing.Point(13, 139)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(201, 34)
		self._label2.TabIndex = 1
		self._label2.Text = "Pence: "
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightGreen
		self._label3.Location = System.Drawing.Point(13, 75)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(201, 34)
		self._label3.TabIndex = 2
		self._label3.Text = "Shillings: "
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._textBox1.Location = System.Drawing.Point(220, 22)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(219, 20)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._textBox2.Location = System.Drawing.Point(220, 147)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(219, 20)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._textBox3.Location = System.Drawing.Point(220, 83)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(219, 20)
		self._textBox3.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Turquoise
		self._button1.Location = System.Drawing.Point(13, 243)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(118, 55)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Turquoise
		self._button2.Location = System.Drawing.Point(410, 243)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(118, 55)
		self._button2.TabIndex = 7
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Turquoise
		self._button3.Location = System.Drawing.Point(211, 243)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(118, 55)
		self._button3.TabIndex = 8
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DeepSkyBlue
		self._label4.Location = System.Drawing.Point(164, 192)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(201, 34)
		self._label4.TabIndex = 9
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkGreen
		self.ClientSize = System.Drawing.Size(573, 310)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang65h"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pnds = int(self._textBox1.Text)
		shil = int(self._textBox2.Text)
		pen = int(self._textBox3.Text)
		decp = pnds  + shil/20 + pen/12/20
		self.label4.Text = "Result:" + decp
		
		

	def Button3Click(self, sender, e):
		self.textBox1.Text = ""
		self.textBox2.Text = ""
		self.textBox3.Text = ""
		
		

	def Button2Click(self, sender, e):
		Application.Exit()