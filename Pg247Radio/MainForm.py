import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.Color.SeaShell
		self._radioButton1.Location = System.Drawing.Point(61, 44)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(145, 37)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "radioButton1"
		self._radioButton1.UseVisualStyleBackColor = False
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.Color.SeaShell
		self._radioButton2.Location = System.Drawing.Point(61, 120)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(145, 37)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "radioButton2"
		self._radioButton2.UseVisualStyleBackColor = False
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.Color.SeaShell
		self._radioButton3.Location = System.Drawing.Point(61, 196)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(145, 37)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "radioButton3"
		self._radioButton3.UseVisualStyleBackColor = False
		# 
		# checkBox1
		# 
		self._checkBox1.BackColor = System.Drawing.Color.Moccasin
		self._checkBox1.Location = System.Drawing.Point(431, 44)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(142, 37)
		self._checkBox1.TabIndex = 3
		self._checkBox1.Text = "checkBox1"
		self._checkBox1.UseVisualStyleBackColor = False
		# 
		# checkBox2
		# 
		self._checkBox2.BackColor = System.Drawing.Color.Moccasin
		self._checkBox2.Location = System.Drawing.Point(431, 120)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(142, 37)
		self._checkBox2.TabIndex = 4
		self._checkBox2.Text = "checkBox2"
		self._checkBox2.UseVisualStyleBackColor = False
		# 
		# checkBox3
		# 
		self._checkBox3.BackColor = System.Drawing.Color.Moccasin
		self._checkBox3.Location = System.Drawing.Point(431, 196)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(142, 37)
		self._checkBox3.TabIndex = 5
		self._checkBox3.Text = "checkBox3"
		self._checkBox3.UseVisualStyleBackColor = False
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkGoldenrod
		self._button1.Location = System.Drawing.Point(24, 323)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(200, 105)
		self._button1.TabIndex = 6
		self._button1.Text = "Ok"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkGoldenrod
		self._button2.Location = System.Drawing.Point(430, 323)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(200, 105)
		self._button2.TabIndex = 7
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkOrange
		self._label1.Location = System.Drawing.Point(63, 6)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(142, 27)
		self._label1.TabIndex = 8
		self._label1.Text = "Radio Buttons"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkOrange
		self._label2.Location = System.Drawing.Point(431, 6)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(142, 27)
		self._label2.TabIndex = 9
		self._label2.Text = "Exit"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MistyRose
		self.ClientSize = System.Drawing.Size(657, 431)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Name = "MainForm"
		self.Text = "Pg247Radio"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		if self._radioButton1.Checked == True:
			strMessage = "You selected Choice 1"
		elif self._radioButton2.Checked == True:
			strMessage = "You selected Choice 2"
		elif self._radioButton3.Checked == True:
			strMessage = "You selected Choice 3"
			
		
		if self._checkBox1.Checked == True:
			strMessage += " and Choice 4"
		elif self._checkBox2.Checked == True:
			strMessage += " and Choice 5"
		elif self._checkBox3.Checked == True:
			strMessage += " and Choice 6"
		MessageBox.Show(strMessage)

	def Button2Click(self, sender, e):
		Application.Exit()