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
		self._listBox1.BackColor = System.Drawing.Color.SeaGreen
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(12, 11)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(589, 303)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Plum
		self._button1.Location = System.Drawing.Point(11, 338)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(176, 109)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Plum
		self._button2.Location = System.Drawing.Point(202, 338)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(176, 109)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Plum
		self._button3.Location = System.Drawing.Point(397, 338)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(176, 109)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DeepPink
		self.ClientSize = System.Drawing.Size(613, 465)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog122b"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Hours\t\tPay"
		self._listBox1.Items.Add(heading)
		for num in range(1, 40+1):
			hours = num + 1
			pay = hours * num
			msg = str(pay) + "\t\t" + str(hours)
			
			self._listBox1.Items.Add(msg)

	def Button2Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()