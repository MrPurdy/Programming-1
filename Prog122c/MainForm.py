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
		self._listBox1.BackColor = System.Drawing.Color.PaleGreen
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(7, 6)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(526, 290)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.OliveDrab
		self._button1.Location = System.Drawing.Point(7, 302)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(174, 94)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.OliveDrab
		self._button2.Location = System.Drawing.Point(180, 302)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(174, 94)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.OliveDrab
		self._button3.Location = System.Drawing.Point(360, 302)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(174, 94)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkOliveGreen
		self.ClientSize = System.Drawing.Size(546, 406)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog122c"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Collum1\t\tCollum2\t\tCollum3\t\tCollum4"
		self._listBox1.Items.Add(heading)
		for num in range(1, 5+1):
			col1 = 1 
			col2 = col1 + 1
			col3 = col1 *2
			col4 = col1**2
			col = str(col1) + "\t\t" + str(col2) + "\t\t" + str(col3) + "\t\t" + str(col4)
			
			self._listBox1.Items.Add(col)
			
	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()