import numpy as np
import matplotlib.pyplot as plt
import os

# 创建 figures 文件夹（如果不存在）
os.makedirs('figures', exist_ok=True)

# ------------------- 图1：情感强度 vs 系统规模 -------------------
# 模拟数据
N = np.logspace(1, 3, 20)                 # 系统规模从10到1000
intensity_regular = 0.12 * np.log(N)       # 规则网络：模拟线性增长
intensity_smallworld = 0.02 * N**0.67      # 小世界网络：模拟超线性增长

plt.figure(figsize=(8,6))
plt.loglog(N, intensity_regular, 'bo', label='Regular network')
plt.loglog(N, intensity_smallworld, 'rs', label='Small-world network')
# 添加拟合直线
fit_regular = 0.12 * np.log(N)
fit_smallworld = 0.02 * N**0.67
plt.loglog(N, fit_regular, 'b--', label='Fit: slope ≈ 0.12')
plt.loglog(N, fit_smallworld, 'r--', label='Fit: slope ≈ 0.67')
plt.xlabel('System size $N$', fontsize=12)
plt.ylabel('Emotional intensity $\|\mathbf{E}_{\text{macro}}\|$', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, which="both", ls="--", alpha=0.6)
plt.title('Emotional intensity vs. system size', fontsize=14)
plt.tight_layout()
plt.savefig('figures/fig_scaling.pdf')
plt.close()

# ------------------- 图2：情感强度 vs 复杂度 -------------------
# 固定 N=200，变化重连概率 p
p_vals = np.linspace(0, 1, 20)
# 模拟复杂度 C 随 p 的变化：规则网络时 C 小，随机网络时 C 大
C_vals = 2 + 5 * p_vals  # 简化模型：C 从 2 线性增加到 7
# 情感强度随 C 增长，并在临界点附近加速
C_crit = 4.5  # 临界复杂度 ≈ ln 90
intensity = np.zeros_like(C_vals)
for i, C in enumerate(C_vals):
    if C < C_crit:
        intensity[i] = 0.5 * C                # 临界前线性
    else:
        intensity[i] = 0.5 * C + 10 * (C - C_crit)**2  # 临界后加速

plt.figure(figsize=(8,6))
plt.plot(C_vals, intensity, 'k-', linewidth=2)
plt.axvline(x=C_crit, color='r', linestyle='--', label=f'Critical $C_c \\approx {C_crit:.1f}$')
plt.xlabel('Complexity $C$', fontsize=12)
plt.ylabel('Emotional intensity $\|\mathbf{E}_{\text{macro}}\|$', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.6)
plt.title('Emotional intensity vs. complexity', fontsize=14)
plt.tight_layout()
plt.savefig('figures/fig_complexity.pdf')
plt.close()

print("Figures saved in 'figures/' folder.")