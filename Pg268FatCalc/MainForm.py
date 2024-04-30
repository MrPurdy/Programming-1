import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.PeachPuff
		self._label1.Location = System.Drawing.Point(39, 36)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(201, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter the number of calories in the food:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(270, 39)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(270, 108)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 3
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.PeachPuff
		self._label2.Location = System.Drawing.Point(39, 105)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(201, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Enter the number of fat grams in the food"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightSalmon
		self.ClientSize = System.Drawing.Size(452, 397)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg268FatCalc"
		self.ResumeLayout(False)
		self.PerformLayout()

