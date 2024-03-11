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
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.OliveDrab
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(159, 29)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter Purchase Price:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.OliveDrab
		self._label2.Location = System.Drawing.Point(12, 57)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(159, 29)
		self._label2.TabIndex = 1
		self._label2.Text = "Enter Amount Received:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Lime
		self._label3.Location = System.Drawing.Point(12, 98)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(159, 29)
		self._label3.TabIndex = 2
		self._label3.Text = "Change Due:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Aqua
		self._button1.Location = System.Drawing.Point(186, 225)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(90, 62)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Aqua
		self._button2.Location = System.Drawing.Point(293, 225)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(90, 62)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.SkyBlue
		self._textBox1.Location = System.Drawing.Point(177, 14)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(172, 20)
		self._textBox1.TabIndex = 6
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.SkyBlue
		self._textBox2.Location = System.Drawing.Point(177, 62)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(172, 20)
		self._textBox2.TabIndex = 7
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightSeaGreen
		self._label4.Location = System.Drawing.Point(12, 138)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(159, 21)
		self._label4.TabIndex = 8
		self._label4.Text = "Dollars:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightSeaGreen
		self._label5.Location = System.Drawing.Point(12, 168)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(159, 19)
		self._label5.TabIndex = 9
		self._label5.Text = "Quarters:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightSeaGreen
		self._label6.Location = System.Drawing.Point(12, 198)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(159, 19)
		self._label6.TabIndex = 10
		self._label6.Text = "Dimes:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.LightSeaGreen
		self._label7.Location = System.Drawing.Point(12, 225)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(159, 17)
		self._label7.TabIndex = 11
		self._label7.Text = "Nickels:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.LightSeaGreen
		self._label8.Location = System.Drawing.Point(12, 248)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(159, 17)
		self._label8.TabIndex = 12
		self._label8.Text = "Pennies:"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Moccasin
		self.ClientSize = System.Drawing.Size(395, 284)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog58t"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pur = float(self._textBox1.Text)
		amo = float(self._textBox2.Text)
		due = amo - pur
		self._label3.Text = "Change Due: " + str(due)
		
		dol = due // 1
		self._label4.Text = "Dollars: " + str(dol) 
		
		quar = (due - dol) // 0.25
		self._label5.Text = "Quarters: " + str(quar)
		
		dim = ((due - dol) - (quar * 0.25)) // 0.1
		self._label6.Text = "Dimes: " + str(dim)
		
		nic = ((due - dol) - (quar * 0.25) - (dim * 0.1)) // 0.05
		self._label7.Text = "Nickels: " + str(nic)
		
		pen = ((due - dol) - (quar * 0.25) - (dim * 0.1) - (nic * 0.05)) // 0.01
		self._label8.Text = "Pennies: " + str(pen)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label3.Text = "Change Due: "
		self._label4.Text = "Dollars: "
		self._label5.Text = "Quarters: "
		self._label6.Text = "Dimes: "
		self._label7.Text = "Nickels: "
		self._label8.Text = "Pennies: "