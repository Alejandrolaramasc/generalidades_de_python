# %%

def raiz_newton_raphson(a, tol=1e-1):
  x0 = a
  x1 = x0 - (x0 ** 2 - a) / (2 * x0)

  while not abs(x1 - x0) <= tol:
      x0 = x1
      x1 = x0 - (x0 ** 2 - a) / (2 * x0)

  return x1

print(f"La raiz de 2 es {raiz_newton_raphson(2)}")
print(f"La raiz de 25 es {raiz_newton_raphson(25)}")
print(f"La raiz de 19 es {raiz_newton_raphson(19)}")

# %%
