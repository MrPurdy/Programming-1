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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.MistyRose
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 22)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(215, 51)
		self._label1.TabIndex = 0
		self._label1.Text = "Number of Guests:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.MistyRose
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 104)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(215, 51)
		self._label2.TabIndex = 1
		self._label2.Text = "Number of Chairs:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.MistyRose
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 186)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(215, 51)
		self._label3.TabIndex = 2
		self._label3.Text = "Permeations:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.MistyRose
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 257)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(215, 51)
		self._label4.TabIndex = 3
		self._label4.Text = "Guests Standing:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.PaleVioletRed
		self._textBox1.Location = System.Drawing.Point(233, 36)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(224, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.PaleVioletRed
		self._textBox2.Location = System.Drawing.Point(233, 122)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(224, 20)
		self._textBox2.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Gold
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(23, 335)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(144, 71)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Gold
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(212, 335)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(147, 71)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Gold
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(403, 335)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(159, 71)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MediumSeaGreen
		self.ClientSize = System.Drawing.Size(574, 418)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog162h"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		guest = int(self._textBox1.Text)
		chair = int(self._textBox2.Text)
		stand = guest - chair
		perm = guest * (guest - 1) * (guest - 2) * (guest - 3)
		self._label3.Text = "Permutation: " + str(perm)
		self._label4.Text = "Guests Standing: " + str(stand)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label3.Text = "Permutation: "
		self._label4.Text = "Guests Standing: "

	def Button3Click(self, sender, e):
		Application.Exit()