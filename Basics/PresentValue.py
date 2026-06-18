from math import exp


def future_discrete_value(x, r, n):
    return x*(1+r)**n


def present_discrete_value(x, r, n):
    return x*(1+r)**-n


def future_continuous_value(x, r, t):
    return x*exp(r*t)


def present_continuous_value(x, r, t):
    return x*exp(-r*t)


if __name__ == '__main__':
    x = 100
    r = 0.05
    n = 5

    print("Future value (discrete model) of x: %s" % future_discrete_value(x, r, n))
    print("Present value (discrete model) of x: %s" % present_discrete_value(x, r, n))
    print("Future value (continuous model) of x: %s" % future_continuous_value(x, r, n))
    print("Present values (continuous model) of x: %s" % present_continuous_value(x, r, n))







