import numpy as np
import matplotlib.pyplot as plt

# Definimos la función a integrar
def f(x):
    return x**2 + 3*x + 1  # Función del ejercicio

# Implementación de la regla del trapecio
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n+1)  # Puntos equidistantes
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])  # Regla del trapecio compuesta
    return integral, x, y

# Solución analítica exacta
def exact_integral(a, b):
    # Integral indefinida: (1/3)x³ + (3/2)x² + x + C
    return (1/3)*b**3 + (3/2)*b**2 + b - ((1/3)*a**3 + (3/2)*a**2 + a)

# Parámetros de integración
a, b = 0, 2  # Intervalo de integración
n_values = [10, 20, 50]  # Números de subdivisiones a probar

# Cálculo exacto
exact_value = exact_integral(a, b)
print(f"Valor exacto de la integral: {exact_value:.6f}\n")

# Resultados para diferentes n
results = []
for n in n_values:
    integral_approx, x_vals, y_vals = trapezoidal_rule(a, b, n)
    error = abs(integral_approx - exact_value)
    results.append((n, integral_approx, error))
    print(f"n = {n}: Aproximación = {integral_approx:.6f}, Error = {error:.6f}")

# Gráfica de la función y la aproximación por trapecios (para n=10 como ejemplo)
x_fine = np.linspace(a, b, 100)
y_fine = f(x_fine)
n_plot = 10
integral_plot, x_plot, y_plot = trapezoidal_rule(a, b, n_plot)

plt.figure(figsize=(10, 6))
plt.plot(x_fine, y_fine, 'r-', label=r'$f(x) = x^2 + 3x + 1$', linewidth=2)
plt.fill_between(x_plot, y_plot, alpha=0.3, color='blue', label="Aproximación Trapecios")
plt.plot(x_plot, y_plot, 'bo-', label=f"Puntos (n={n_plot})")

# Etiquetas y leyenda
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("Aproximación de la integral con la regla del trapecio")
plt.legend()
plt.grid()

# Guardar la figura
plt.savefig("trapecio_polinomio.png")
plt.show()

# Gráfica de error vs número de subintervalos
plt.figure(figsize=(8, 5))
n_list = [r[0] for r in results]
error_list = [r[2] for r in results]
plt.plot(n_list, error_list, 'bo-')
plt.xlabel("Número de subintervalos (n)")
plt.ylabel("Error absoluto")
plt.title("Convergencia del método del trapecio")
plt.grid()
plt.savefig("convergencia_trapecio.png")
plt.show()