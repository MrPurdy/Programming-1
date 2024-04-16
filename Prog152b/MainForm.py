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
		self._listBox1 = System.Windows.Forms.ListBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightSkyBlue
		self._button1.Location = System.Drawing.Point(12, 373)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(254, 112)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightSkyBlue
		self._button2.Location = System.Drawing.Point(282, 373)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(254, 112)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightSkyBlue
		self._button3.Location = System.Drawing.Point(553, 373)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(254, 112)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.SkyBlue
		self._label1.Location = System.Drawing.Point(15, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(233, 38)
		self._label1.TabIndex = 3
		self._label1.Text = "Enter your test value:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.LightBlue
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(12, 68)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(508, 290)
		self._listBox1.TabIndex = 4
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Yellow
		self._textBox1.Location = System.Drawing.Point(254, 19)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(254, 20)
		self._textBox1.TabIndex = 5
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightSeaGreen
		self.ClientSize = System.Drawing.Size(819, 497)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog152b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		for num in range():

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		

	def Button3Click(self, sender, e):
		Application.Exit()