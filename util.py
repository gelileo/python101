def demo(func, desc: str):
  print('=' * (len(desc) + 10))
  print(f" Demo of {desc} ")
  print('=' * (len(desc) + 10))
  print()
  func()
  print()
