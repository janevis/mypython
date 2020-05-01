count = int (input("Введите количество пингвинов: ")) #в этой строке я создаю переменную count чтобы получить число пингвинов
while count < 0 or count > 9: count = int (input("Введите количество пингвинов от 0 до 9: ")) #в этой строке я делаю проверку что число в диапазоне 0 - 9

print("   _~_    " * count)    
print("  (o o)   " * count)
print(" /  v  \\  " * count)
print("/(  _  )\\ " * count)
print("  ^^ ^^   " * count)
