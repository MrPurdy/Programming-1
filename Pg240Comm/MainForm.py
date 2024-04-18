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
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label9 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Bisque
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(142, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(233, 56)
		self._label1.TabIndex = 0
		self._label1.Text = "Sales for the month:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Bisque
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(125, 84)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(250, 56)
		self._label2.TabIndex = 1
		self._label2.Text = "Advanced pay rewarded:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Bisque
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(192, 162)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(233, 56)
		self._label3.TabIndex = 2
		self._label3.Text = "Commission Rate:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Bisque
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(192, 232)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(233, 56)
		self._label4.TabIndex = 3
		self._label4.Text = "Commission:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Bisque
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(192, 301)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(233, 56)
		self._label5.TabIndex = 4
		self._label5.Text = "Net Pay:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Bisque
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(464, 162)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(233, 56)
		self._label6.TabIndex = 5
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Bisque
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(464, 232)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(233, 56)
		self._label7.TabIndex = 6
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Bisque
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(464, 301)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(233, 56)
		self._label8.TabIndex = 7
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.PowderBlue
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(49, 362)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(168, 66)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.PowderBlue
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(277, 362)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(168, 66)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.PowderBlue
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(496, 362)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(168, 66)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.SpringGreen
		self._textBox1.Location = System.Drawing.Point(398, 31)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(255, 20)
		self._textBox1.TabIndex = 11
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.SpringGreen
		self._textBox2.Location = System.Drawing.Point(398, 106)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(255, 20)
		self._textBox2.TabIndex = 12
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Bisque
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(431, 152)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(294, 207)
		self._label9.TabIndex = 13
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Turquoise
		self.ClientSize = System.Drawing.Size(723, 440)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg240Comm"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		decSalesAmount = 0.0
		decAdvancedPayAmount = 0.0
		decCommissionRate = 0.0
		decCommissionAmount = 0.0
		decNetPay = 0.0
		
		try:
			decSalesAmount = float(self._textBox1.Text)
			except:
				self._label9.Text = "Sales amount must be numeric"
				self._label9.Text.Visible = True
				return
		
		if dec

	def Button2Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		pass