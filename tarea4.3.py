import numpy as np
import matplotlib.pyplot as plt

# Definimos la función a integrar
def f(x):
    return np.sin(x)  # Función seno

# Implementación de la regla del trapecio
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n+1)  # Puntos equidistantes
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])  # Regla del trapecio compuesta
    return integral, x, y

# Parámetros de integración
a, b = 0, 1  # Intervalo de integración [0,1]
n_values = [5, 10, 20, 50]  # Valores de n a probar

# Solución analítica exacta
exact_value = -np.cos(1) - (-np.cos(0))  # Integral de sin(x) es -cos(x)
print(f"Valor exacto de la integral: {exact_value:.6f}\n")

# Resultados para diferentes n
results = []
for n in n_values:
    integral_approx, x_vals, y_vals = trapezoidal_rule(a, b, n)
    error = abs(integral_approx - exact_value)
    results.append((n, integral_approx, error))
    print(f"n = {n}: Aproximación = {integral_approx:.6f}, Error = {error:.6f}")

# Gráfica de la función y las aproximaciones
plt.figure(figsize=(12, 8))
x_fine = np.linspace(a, b, 100)
y_fine = f(x_fine)

# Graficar función exacta
plt.plot(x_fine, y_fine, 'k-', label=r'$f(x) = \sin(x)$', linewidth=2)

# Graficar aproximaciones para cada n
colors = ['r', 'g', 'b', 'm']
for i, n in enumerate(n_values):
    _, x_plot, y_plot = trapezoidal_rule(a, b, n)
    plt.plot(x_plot, y_plot, colors[i]+'o--', label=f'Aprox. n={n}', alpha=0.7)

# Configuración del gráfico
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Aproximación de $\int_0^1 \sin(x)dx$ con la regla del trapecio')
plt.legend()
plt.grid(True)
plt.savefig('trapecio_seno.png')
plt.show()

# Gráfica de convergencia
plt.figure(figsize=(10, 6))
n_list = [r[0] for r in results]
error_list = [r[2] for r in results]
plt.plot(n_list, error_list, 'bo-')
plt.xlabel('Número de subintervalos (n)')
plt.ylabel('Error absoluto')
plt.title('Convergencia del método del trapecio para $\sin(x)$')
plt.grid(True)
plt.savefig('convergencia_seno.png')
plt.show()