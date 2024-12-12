import numpy as np 
import matplotlib.pyplot as plt 

def estimate_coef(x, y):
    #number of points
    n = np.size(x)

    #mean of x, y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    #calculating cross-deviation and deviation of x
    SS_xy = np.sum(y*x) - n * m_x * m_y
    SS_xx = np.sum(x*x) - n * m_x * m_x

    #calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)

def plot_regression_line(x, y, b):
    plt.scatter(x, y, 
                color = 'm',
                marker = 'o',
                s = 30
                )

    #predict response vector
    y_pred = b[1] * x + b[0]

    # plotting the regression line
    plt.plot(x, y_pred)
 
    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def main():
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients:")
    count = 0
    for i in b:
        print("p_{} = {}".format(count, i))
        count += 1

    plot_regression_line(x, y, b)

main()