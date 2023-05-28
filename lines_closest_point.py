#!/usr/bin/python3

import numpy as np

def intersect(P0,P1):
    """P0 and P1 are NxD arrays defining N lines.
    D is the dimension of the space. This function 
    returns the least squares intersection of the N
    lines from the system given by eq. 13 in 
    http://cal.cs.illinois.edu/~johannes/research/LS_line_intersect.pdf.
    """
    # generate all line direction vectors 
    n = (P1-P0)/np.linalg.norm(P1-P0,axis=1)[:,np.newaxis] # normalized

    # generate the array of all projectors 
    projs = np.eye(n.shape[1]) - n[:,:,np.newaxis]*n[:,np.newaxis]  # I - n*n.T
    # see fig. 1 

    # generate R matrix and q vector
    R = projs.sum(axis=0)
    q = (projs @ P0[:,:,np.newaxis]).sum(axis=0)
    # q = P0[:,:,np.newaxis].sum(axis=0)

    # solve the least squares problem for the 
    # intersection point p: Rp = q
    print(q)
    print(R)
    p = np.linalg.lstsq(R,q,rcond=0.001)[0]

    return p

# def get_line_params(x11, x12, y11, y12):
#     A = y12 - y11
#     B = x12 - x11
#     C = x11 * y12 - x12 * y11
#     return A, B, C

# x3 = 13
# y1 = 13
# r1 = 14
# r2 = 2.25
# r3 = 15

# # Example usage:
# x11 = -2.085
# x12 = -x11
# y11 = -0.84

# x21 = -1.95
# y21 = -1.106
# y22 = -y21

# # get line coordinates from these two points
# a1, b1, c1 = get_line_params(x11, x12, y11, y11)
# a2, b2, c2 = get_line_params(x21, x21, y21, y22)
# a3 = x3 / y1
# b3 = -1
# c3 = - (r1 ** 2 - r3 ** 2 + x3 ** 2 - y1 ** 2) / (2 * y1)


# line1 = [a1, b1, c1]  # Equation of the first line: 2.5x + 1.5y - 0.5 = 0
# line2 = [a2, b2, c2]  # Equation of the second line: -1.2x + 0.8y + 2.5 = 0
# line3 = [a3, b3, c3]  # Equation of the third line: 0.5x - 0.5y - 2.5 = 0


# lines = [line1, line2, line3]

n = 6
# P0 = np.stack((np.array([5,5])+3*np.random.random(size=2) for i in range(n)))
# a = np.linspace(0,2*np.pi,n)+np.random.random(size=n)*np.pi/5.0
# P1 = np.array([5+5*np.sin(a),5+5*np.cos(a)]).T

            #   p11  p21
P0 = np.array([[-2, -2], 
               [-1, -1]])
            #   p12 p22 
P1 = np.array([[0, 13], 
               [13, 0]])
closest_point = intersect(P0, P1)
print(f"The closest point is {closest_point}")

