import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Plum
		self._label1.Location = System.Drawing.Point(16, 14)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(626, 199)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Fuchsia
		self._button1.Location = System.Drawing.Point(12, 241)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(178, 95)
		self._button1.TabIndex = 1
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Fuchsia
		self._button2.Location = System.Drawing.Point(235, 241)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(198, 94)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Fuchsia
		self._button3.Location = System.Drawing.Point(469, 241)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(172, 94)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightSeaGreen
		self.ClientSize = System.Drawing.Size(660, 351)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Favorite Quote"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"

	def Button2Click(self, sender, e):
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()