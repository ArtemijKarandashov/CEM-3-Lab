def half_life(N0, t, t_half):
  """Вычисляет количество радиоактивного вещества через время t"""
  return N0 * (1 / 2)**(t / t_half)


def curry_half_life(t_half):
  """Возвращает функцию, вычисляющую количество радиоактивного вещества для данного изотопа"""
  def inner(N0, t):
      return half_life(N0, t, t_half)
  return inner


# Периоды полураспада изотопов в годах
isotopes = {
  "U-238": curry_half_life(4.468 * 10**9),
  "Ra-226": curry_half_life(1600),
  "T": curry_half_life(12.3),
}


def user_input():
  """Запрашивает ввод пользователя и вычисляет количество радиоактивного вещества"""
  N0 = float(input("Начальное количество радиоактивного вещества: "))
  t = float(input("Момент времени (в годах): "))

  for isotope in isotopes:
      N = isotopes[isotope](N0, t)
      print(f"Для изотопа {isotope} в момент времени {t} осталось {N}")