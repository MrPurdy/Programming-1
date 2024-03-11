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
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label1.Location = System.Drawing.Point(6, 18)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(243, 47)
		self._label1.TabIndex = 0
		self._label1.Text = "Kilowatts"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label2.Location = System.Drawing.Point(176, 202)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(243, 47)
		self._label2.TabIndex = 1
		self._label2.Text = "Citytax: "
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label3.Location = System.Drawing.Point(176, 146)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(243, 47)
		self._label3.TabIndex = 2
		self._label3.Text = "Surcharge: "
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.PaleVioletRed
		self._button1.Location = System.Drawing.Point(6, 392)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(162, 76)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.PaleVioletRed
		self._button2.Location = System.Drawing.Point(221, 392)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(162, 76)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.PaleVioletRed
		self._button3.Location = System.Drawing.Point(439, 392)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(162, 74)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Pink
		self._textBox1.Location = System.Drawing.Point(292, 32)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(242, 20)
		self._textBox1.TabIndex = 6
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label4.Location = System.Drawing.Point(12, 258)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(243, 47)
		self._label4.TabIndex = 9
		self._label4.Text = "Pay this amount:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label5.Location = System.Drawing.Point(358, 258)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(243, 47)
		self._label5.TabIndex = 10
		self._label5.Text = "After May 20th:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label6.Location = System.Drawing.Point(176, 86)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(243, 47)
		self._label6.TabIndex = 11
		self._label6.Text = "Base Rate:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Tomato
		self.ClientSize = System.Drawing.Size(681, 480)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog93a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		kilowatts = int(self._textBox1.Text)
		base = kilowatts * 0.0475
		sur = base * 0.1
		citytax = base * 0.03
		amount = base + sur + citytax
		after = amount * 0.04 + amount
		self._label1.Text = "Kilowatts: " + str(kilowatts)
		self._label2.Text = "Surcharge: " + str(sur)
		self._label3.Text = "Citytax: " + str(citytax)
		self._label4.Text = "Pay this amount: " + str(amount)
		self._label5.Text = "After May 20th: " + str(after)
		self._label6.Text = "Base Rate: " + str(base)
		base = round(base, 2)
		sur = round(sur, 2)
		citytax = round(citytax, 2)
		amount = round(amount, 2)
		after = round(after, 2)

	def Button2Click(self, sender, e):
		self._label1.Text = "Kilowatts:"
		self._label2.Text = "Surcharge:"
		self._label3.Text = "Citytax:"
		self._label4.Text = "Pay this amount:"
		self._label5.Text = "After May 20th:"
		self._label6.Text = "Base Rate:"
		self._textBox1.Text = ""
		
		

	def Button3Click(self, sender, e):
		Application.Exit()