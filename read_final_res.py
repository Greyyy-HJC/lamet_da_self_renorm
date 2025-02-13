# %%
import gvar as gv
import matplotlib.pyplot as plt
from head import *

[pi_x, pi_y1, pi_y2] = gv.load('final_plot_pion')
[k_x, k_y1, k_y2] = gv.load('final_plot_kaon')

pi_cv = (pi_y1 + pi_y2) / 2
pi_err_all = abs((pi_y1 - pi_y2) / 2)

k_cv = (k_y1 + k_y2) / 2
k_err_all = abs((k_y1 - k_y2) / 2)

print(pi_x[-10:])
print(len(pi_x))

plt.fill_between(pi_x, pi_y1, pi_y2, color="orange", alpha=0.4)
plt.title('pion')
plt.show()

plt.fill_between(pi_x, pi_cv+pi_err_all, pi_cv-pi_err_all, color="blue", alpha=0.4)
plt.title('pion')
plt.show()


plt.fill_between(k_x, k_y1, k_y2, color="orange", alpha=0.4)
plt.title('kaon')
plt.show()

plt.fill_between(k_x, k_cv+k_err_all, k_cv-k_err_all, color="blue", alpha=0.4)
plt.title('kaon')
plt.show()

# %% int with 1/x, pion
pi_gv = [gv.gvar( (pi_y1[i] + pi_y2[i])/2, abs(pi_y1[i]-pi_y2[i])/2 ) for i in range(len(pi_x)) ]

pi_samp = gv_to_samples(pi_gv, N_samp=100)
print(np.shape(pi_samp))

dx = 0.01
print(pi_x[:10])

val_ls = []
for n in range(100):
    temp = []
    for i in range(1, len(pi_x)): # remove x=0 point
        temp.append( pi_samp[n][i] / pi_x[i] )
        val = np.sum(temp)
        val = val * dx
    val_ls.append(val)

val_avg = gv.dataset.avg_data(val_ls, bstrap=True)

print(val_avg)

# %% int with 1/x, kaon
k_gv = [gv.gvar( (k_y1[i] + k_y2[i])/2, abs(k_y1[i]-k_y2[i])/2 ) for i in range(len(k_x)) ]

k_samp = gv_to_samples(k_gv, N_samp=100)
print(np.shape(k_samp))

dx = 0.01
print(k_x[:10])

val_ls = []
for n in range(100):
    temp = []
    for i in range(1, len(k_x)): # remove x=0 point
        temp.append( k_samp[n][i] / k_x[i] )
        val = np.sum(temp)
        val = val * dx
    val_ls.append(val)

val_avg = gv.dataset.avg_data(val_ls, bstrap=True)

print(val_avg)


# %%
x_tex = [int(v)/100 for v in pi_x * 100][::5][1:-1]
y1 = pi_y1[::5][1:-1]
y2 = pi_y2[::5][1:-1]
pi_tex = [gv.gvar( (y1[i] + y2[i])/2, abs(y1[i]-y2[i])/2 ) for i in range(len(x_tex)) ]

plt.fill_between(pi_x, pi_y1, pi_y2, color="orange", alpha=0.4)
plt.errorbar(x_tex, [v.mean for v in pi_tex], [v.sdev for v in pi_tex], **errorb)
plt.title('pion')
plt.show()

y1 = k_y1[::5][1:-1]
y2 = k_y2[::5][1:-1]
k_tex = [gv.gvar( (y1[i] + y2[i])/2, abs(y1[i]-y2[i])/2 ) for i in range(len(x_tex)) ]

plt.fill_between(k_x, k_y1, k_y2, color="orange", alpha=0.4)
plt.errorbar(x_tex, [v.mean for v in k_tex], [v.sdev for v in k_tex], **errorb)
plt.title('kaon')
plt.show()


# %%
# f = open('temp/pion_err_all.txt', 'w')
# line = []
# line.append('x')
# line.append('\t')
# line.append('cv')
# line.append('\t')
# line.append('err_all')
# line.append('\n')
# f.writelines(line)

# for i in range(len(pi_x)):
#     line = []
#     line.append(str(pi_x[i]))
#     line.append('\t')
#     line.append(str(pi_cv[i]))
#     line.append('\t')
#     line.append(str(pi_err_all[i]))
#     line.append('\n')
#     f.writelines(line)
# f.close


# f = open('temp/kaon_err_all.txt', 'w')
# line = []
# line.append('x')
# line.append('\t')
# line.append('cv')
# line.append('\t')
# line.append('err_all')
# line.append('\n')
# f.writelines(line)

# for i in range(len(k_x)):
#     line = []
#     line.append(str(k_x[i]))
#     line.append('\t')
#     line.append(str(k_cv[i]))
#     line.append('\t')
#     line.append(str(k_err_all[i]))
#     line.append('\n')
#     f.writelines(line)
# f.close


# %%
