from fractions import Fraction
import numpy as np
import matplotlib.pyplot as plt

def encrypt_coefficients(coefficients):
    encrypted_coefficients = [coeff * 2 for coeff in coefficients]  # double the coefficients
    return encrypted_coefficients

def decrypt_coefficients(encrypted_coefficients):
    decrypted_coefficients = [coeff // 2 for coeff in encrypted_coefficients]  # divide the coefficients by 2
    return decrypted_coefficients

def simultaneous_eq(a,b):
    if a[0] == 0:
        y = Fraction(a[2], a[1])
        x = Fraction(b[2] - b[1]*y, b[0])
    elif a[1] == 0:
        x = Fraction(a[2], a[0])
        y = Fraction(b[2] - b[0]*x, b[1])
    elif b[0] == 0:
        y = Fraction(b[2], b[1])
        x = Fraction(a[2] - a[1]*y, a[0])
    elif b[1] == 0:
        x = Fraction(b[2], b[0])
        y = Fraction(a[2] - a[0]*x, a[1])
    else:
        a = np.array(a)
        b = np.array(b)
        c = b * Fraction(a[0], b[0])
        d = a - c
        y = Fraction(d[2], d[1])
        x = Fraction(a[2] - a[1] * y, a[0])
    return x, y

class Linear_function:
    def question(self):
        self.select = np.random.randint(2)
        if self.select == 1:
            self.coefficient = np.random.randint(low=-10, high=10, size=2)
            self.constant = np.random.randint(low=-10, high=10)
            print('find {}x + {}y + {} = 0 of slope, x intercept, and y intercept'.format(self.coefficient[0], self.coefficient[1], self.constant))
            print('Draw the above function when x is from -10 to 10.')
        else:
            self.coefficient = np.random.randint(low=-10, high=10, size=4)
            self.constant = np.random.randint(low=-10, high=10, size=2)
            print('Find the intersection of the following two straight lines and draw the two graphs.')
            print('{}x + {}y + {} = 0'.format(self.coefficient[0], self.coefficient[1], self.constant[0]))
            print('{}x + {}y + {} = 0'.format(self.coefficient[2], self.coefficient[3], self.constant[1]))

        "generate encrypted coefficients"
        self.encrypted_coefficient = encrypt_coefficients(self.coefficient)

    def answer(self):
        if self.select == 1:
            slope = Fraction(-self.coefficient[0], self.coefficient[1])
            y_cross = Fraction(-self.constant, self.coefficient[1])
            print('Slope : {}'.format(Fraction(-self.coefficient[0], self.coefficient[1])))
            print('x intercept : {}'.format(Fraction(-self.constant, self.coefficient[0])))
            print('y intercept : {}'.format(Fraction(-self.constant, self.coefficient[1])))
            x = np.arange(-10, 11)
            y = slope * x + y_cross
            plt.plot(x, y)
            plt.grid()
        else:
            "compute decrypted coefficients"
            decrypted_coefficient = decrypt_coefficients(self.encrypted_coefficient)
            a = decrypted_coefficient[0], decrypted_coefficient[1], -self.constant[0]
            b = decrypted_coefficient[2], decrypted_coefficient[3], -self.constant[1]
            x, y = simultaneous_eq(a, b)
            print(x, y)
            x = np.arange(-10, 11)
            slope1 = Fraction(-decrypted_coefficient[0], decrypted_coefficient[1])
            y_cross1 = Fraction(-self.constant[0], decrypted_coefficient[1])

            slope2 = Fraction(-decrypted_coefficient[2], decrypted_coefficient[3])
            y_cross2 = Fraction(-self.constant[1], decrypted_coefficient[3])
            y1 = slope1 * x + y_cross1
            y2 = slope2 * x + y_cross2
            plt.plot(x, y1, label='{}x + {}y + {} = 0'.format(decrypted_coefficient[0], decrypted_coefficient[1], self.constant[0]))
            plt.plot(x, y2, label='{}x + {}y + {} = 0'.format(decrypted_coefficient[2], decrypted_coefficient[3], self.constant[1]))
            plt.grid()
            plt.legend()
            plt.show()

q1 = Linear_function()
q1.question()
q1.answer()