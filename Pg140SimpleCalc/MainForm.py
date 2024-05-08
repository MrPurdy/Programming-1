import System.Drawing
import System.Windows.Forms
import math

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
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.NavajoWhite
		self._label1.Location = System.Drawing.Point(42, 30)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(190, 38)
		self._label1.TabIndex = 0
		self._label1.Text = "Number 1:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.NavajoWhite
		self._label2.Location = System.Drawing.Point(42, 143)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(190, 33)
		self._label2.TabIndex = 1
		self._label2.Text = "Operation:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.NavajoWhite
		self._label3.Location = System.Drawing.Point(42, 241)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(190, 33)
		self._label3.TabIndex = 2
		self._label3.Text = "Number 2:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.NavajoWhite
		self._label4.Location = System.Drawing.Point(60, 310)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(50, 33)
		self._label4.TabIndex = 3
		self._label4.Text = "Result:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Orange
		self._label5.Location = System.Drawing.Point(118, 310)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(114, 33)
		self._label5.TabIndex = 4
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Goldenrod
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(431, 23)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 52)
		self._button1.TabIndex = 5
		self._button1.Text = "+"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Goldenrod
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25)
		self._button2.Location = System.Drawing.Point(512, 23)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 52)
		self._button2.TabIndex = 6
		self._button2.Text = "-"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Goldenrod
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25)
		self._button3.Location = System.Drawing.Point(593, 23)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 52)
		self._button3.TabIndex = 7
		self._button3.Text = "*"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.Goldenrod
		self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25)
		self._button4.Location = System.Drawing.Point(431, 81)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(75, 52)
		self._button4.TabIndex = 8
		self._button4.Text = "^"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.Color.Goldenrod
		self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25)
		self._button5.Location = System.Drawing.Point(512, 81)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(75, 52)
		self._button5.TabIndex = 9
		self._button5.Text = "/"
		self._button5.UseVisualStyleBackColor = False
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.BackColor = System.Drawing.Color.Goldenrod
		self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25)
		self._button6.Location = System.Drawing.Point(593, 81)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(75, 52)
		self._button6.TabIndex = 10
		self._button6.Text = "//"
		self._button6.UseVisualStyleBackColor = False
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.BackColor = System.Drawing.Color.Goldenrod
		self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(499, 133)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(99, 52)
		self._button7.TabIndex = 11
		self._button7.Text = "MOD"
		self._button7.UseVisualStyleBackColor = False
		self._button7.Click += self.Button7Click
		# 
		# button8
		# 
		self._button8.BackColor = System.Drawing.Color.Gold
		self._button8.Location = System.Drawing.Point(499, 241)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(130, 52)
		self._button8.TabIndex = 12
		self._button8.Text = "Clear"
		self._button8.UseVisualStyleBackColor = False
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.BackColor = System.Drawing.Color.Gold
		self._button9.Location = System.Drawing.Point(499, 300)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(130, 52)
		self._button9.TabIndex = 13
		self._button9.Text = "Exit"
		self._button9.UseVisualStyleBackColor = False
		self._button9.Click += self.Button9Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.BurlyWood
		self._textBox1.Location = System.Drawing.Point(238, 30)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(158, 38)
		self._textBox1.TabIndex = 14
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.BurlyWood
		self._textBox2.Location = System.Drawing.Point(238, 241)
		self._textBox2.Multiline = True
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(158, 33)
		self._textBox2.TabIndex = 15
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SeaShell
		self.ClientSize = System.Drawing.Size(676, 426)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg140SimpleCalc"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
	 	num2 = int(self._textBox2.Text)
	 	add = num1 + num2
		self._label5.Text = " " + str(add)
		self._label2.Text = "Operation: +"

	def Button2Click(self, sender, e):
		num1 = int(self._textBox1.Text)
	 	num2 = int(self._textBox2.Text)
	 	sub = num1 - num2
		self._label5.Text = " " + str(sub)
		self._label2.Text = "Operation: -"

	def Button3Click(self, sender, e):
		num1 = int(self._textBox1.Text)
	 	num2 = int(self._textBox2.Text)
	 	mul = num1 * num2
		self._label5.Text = " " + str(mul)
		self._label2.Text = "Operation: *"

	def Button4Click(self, sender, e):
		num1 = int(self._textBox1.Text)
	 	num2 = int(self._textBox2.Text)
	 	pow = num1 ** num2
		self._label5.Text = " " + str(pow)
		self._label2.Text = "Operation: ^"

	def Button5Click(self, sender, e):
		num1 = int(self._textBox1.Text)
	 	num2 = int(self._textBox2.Text)
	 	div = num1 / num2
		self._label5.Text = " " + str(div)
		self._label2.Text = "Operation: /"

	def Button6Click(self, sender, e):
		num1 = int(self._textBox1.Text)
	 	num2 = int(self._textBox2.Text)
	 	ddiv = num1 // num2
		self._label5.Text = " " + str(ddiv)
		self._label2.Text = "Operation: //"

	def Button7Click(self, sender, e):
		num1 = int(self._textBox1.Text)
	 	num2 = int(self._textBox2.Text)
	 	mod = math.fmod(num1, num2)
		self._label5.Text = " " + str(mod)
		self._label2.Text = "Operation: MOD"

	def Button8Click(self, sender, e):
		self._label5.Text = ""
		self._label2.Text = "Operation: "
		self._textBox1.Text = ""
		self._textBox2.Text = ""

	def Button9Click(self, sender, e):
		Application.Exit()