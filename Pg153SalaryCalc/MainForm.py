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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Goldenrod
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(47, 35)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(247, 54)
		self._label1.TabIndex = 0
		self._label1.Text = "Annual Salary:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Goldenrod
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(47, 145)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(247, 54)
		self._label2.TabIndex = 1
		self._label2.Text = "Pay period per year:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Goldenrod
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(47, 252)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(247, 54)
		self._label3.TabIndex = 2
		self._label3.Text = "Salary per pay period:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Goldenrod
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(328, 252)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(247, 54)
		self._label4.TabIndex = 3
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Orange
		self._textBox1.Location = System.Drawing.Point(300, 56)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(263, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Orange
		self._textBox2.Location = System.Drawing.Point(312, 166)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(263, 20)
		self._textBox2.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.PaleGoldenrod
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(215, 330)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(176, 72)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.BurlyWood
		self.ClientSize = System.Drawing.Size(630, 414)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg153SalaryCalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		decAnnualSalary = 0.0
		intPayPeriods = 0
		decSalary = 0.0
		
		try:
			decAnnualSalary = float(self._textBox1.Text)
			intPayPeriods = int(self._textBox2.Text)
		except:
			MessageBox.Show("The input files must contain nonzero numeric values.", "Error")
		
		decSalary = decAnnualSalary / intPayPeriods
		self._label4.Text = str(round(decSalary, 2))