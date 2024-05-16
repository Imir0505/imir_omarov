import sys
# сохраняем старый поток вывода
old_stderr = sys.stderr
# перенаправляем поток вывода в файл output.txt
new_stderr = open('outerr.txt', 'w')
sys.stderr = new_stderr
# теперь print будет выводить в файл
raise Exception('Hello stderr.txt')
# закрываем файл и возвращаем старый поток вывода
new_stderr.close()
sys.stderr = old_stderr
raise Exception('Hello stderr')