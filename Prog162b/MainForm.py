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
		self._listBox1.BackColor = System.Drawing.Color.Lime
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(528, 264)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Orchid
		self._button1.Location = System.Drawing.Point(18, 297)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(161, 88)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Orchid
		self._button2.Location = System.Drawing.Point(201, 297)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(161, 88)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Orchid
		self._button3.Location = System.Drawing.Point(379, 297)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(161, 88)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Turquoise
		self.ClientSize = System.Drawing.Size(547, 393)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog162b"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Year\t\tPopulation (in mil.)"
		self._listBox1.Items.Add(heading)
		pop = 243
		for year in range(1990, 2016):
			line = str(year) + "\t\t" + str(int(pop))
			self._listBox1.Items.Add(line)
			pop *= 1.029

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Applicaton.Exit()