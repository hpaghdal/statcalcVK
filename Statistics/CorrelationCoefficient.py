from Statistics.PopulationMean import mean
from Statistics.StandardDeviation import st_dev
from Calculator.Multiplication import multiplication
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Statistics.SampleMean import samp_mean


def Pop_correlation_coefficient():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x_data = [1, 25, 34, 4, 51]
    y_data = [6, 7, 8, 9, 10]
    x_mean = mean(x_data)
    y_mean = mean(y_data)
    a = []
    b = []
    ab = []
    x = st_dev(x_data)
    y = st_dev(y_data)
    divisor = multiplication(x, y)
    z = len(lst)

    for i in x_data:
        new1 = subtraction(x_mean, i)
        zx = division(new1, x)
        a.append(zx)

        # (zx)i = (xi – x̄) / s x
    for i in y_data:
        new2 = subtraction(y_mean, i)
        zy = division(new2, y)
        b.append(zy)

    ab = [a[i] * b[i] for i in range(len(x_data))]

    tot_sum = sum(ab)
    result = tot_sum / 4

    return result

# covriance = cov(X, Y) = (sum (x - mean(X)) * (y - mean(Y)) ) * 1/(n-1)
# covariance(X, Y) / (stdv(X) * stdv(Y))
