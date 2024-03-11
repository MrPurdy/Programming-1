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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightCoral
		self._label1.Location = System.Drawing.Point(10, 17)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(207, 38)
		self._label1.TabIndex = 0
		self._label1.Text = "Length"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightCoral
		self._label2.Location = System.Drawing.Point(10, 89)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(207, 38)
		self._label2.TabIndex = 1
		self._label2.Text = "Width"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Bisque
		self._textBox1.Location = System.Drawing.Point(251, 27)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(236, 20)
		self._textBox1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Bisque
		self._textBox2.Location = System.Drawing.Point(251, 107)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(236, 20)
		self._textBox2.TabIndex = 3
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Cornsilk
		self._button1.Location = System.Drawing.Point(20, 270)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(179, 78)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Cornsilk
		self._button2.Location = System.Drawing.Point(229, 270)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(179, 78)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Cornsilk
		self._button3.Location = System.Drawing.Point(438, 270)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(179, 78)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightCoral
		self._label3.Location = System.Drawing.Point(10, 155)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(207, 38)
		self._label3.TabIndex = 7
		self._label3.Text = "Area: "
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightCoral
		self._label4.Location = System.Drawing.Point(10, 212)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(207, 38)
		self._label4.TabIndex = 8
		self._label4.Text = "Perimeter: "
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Peru
		self.ClientSize = System.Drawing.Size(629, 367)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang52a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		length = int(self._textBox1.Text)
		width = int(self._textBox2.Text)
		area = length * width
		perim = 2 * length + 2 * width
		self._label3.Text = str(area)
		self._label4.Text = str(perim)