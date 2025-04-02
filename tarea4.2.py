import numpy as np
import matplotlib.pyplot as plt

# Definimos la función a integrar (Gaussiana)
def f(x):
    return np.exp(-x**2)

# Implementación de la regla del trapecio
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n+1)  # Puntos equidistantes
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])  # Regla del trapecio compuesta
    return integral, x, y

# Parámetros de integración
a, b = 0, 1  # Intervalo de integración [0,1] - asumido ya que no se especificó
n_values = [5, 10, 15]  # Números de subdivisiones a probar

# Resultados para diferentes n
results = []
for n in n_values:
    integral_approx, x_vals, y_vals = trapezoidal_rule(a, b, n)
    results.append((n, integral_approx))
    print(f"n = {n}: Aproximación = {integral_approx:.6f}")

# Gráfica de la función y la aproximación por trapecios (para n=5 como ejemplo)
x_fine = np.linspace(a, b, 100)
y_fine = f(x_fine)
n_plot = 5
integral_plot, x_plot, y_plot = trapezoidal_rule(a, b, n_plot)

plt.figure(figsize=(10, 6))
plt.plot(x_fine, y_fine, 'r-', label=r'$f(x) = e^{-x^2}$', linewidth=2)
plt.fill_between(x_plot, y_plot, alpha=0.3, color='blue', label="Aproximación Trapecios")
plt.plot(x_plot, y_plot, 'bo-', label=f"Puntos (n={n_plot})")

# Etiquetas y leyenda
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("Aproximación de la integral con la regla del trapecio")
plt.legend()
plt.grid()

# Guardar la figura
plt.savefig("trapecio_gaussiana.png")
plt.show()

# Gráfica de convergencia
approx_values = [r[1] for r in results]
plt.figure(figsize=(8, 5))
plt.plot(n_values, approx_values, 'bo-')
plt.xlabel("Número de subintervalos (n)")
plt.ylabel("Valor aproximado de la integral")
plt.title("Convergencia de la aproximación")
plt.grid()
plt.savefig("convergencia_gaussiana.png")
plt.show()