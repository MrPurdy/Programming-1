import System.Drawing
import System.Windows.Forms

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
		self._listBox1.BackColor = System.Drawing.Color.Honeydew
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(8, 9)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(596, 290)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Yellow
		self._button1.Location = System.Drawing.Point(8, 320)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(160, 93)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Yellow
		self._button2.Location = System.Drawing.Point(221, 320)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(160, 93)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Yellow
		self._button3.Location = System.Drawing.Point(441, 320)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(160, 93)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Orange
		self.ClientSize = System.Drawing.Size(613, 424)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog122d"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "X\t\tY"
		self._listBox1.Items.Add(heading)
		for num in range(-13, 16):
			x = num + 1
			y = x**6 - 3 * x**5 - 93 * x**4 + 87 * x**3 + 1596 * x**2 - 1380 * x - 2800
			msg = str(x) + "\t\t" + str(y)
			self._listBox1.Items.Add(msg)
	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()
