###Задание 1
import os
import subprocess
import time


def find_process_using_port(port):
    """Возвращает PID процесса, занимающего указанный порт, или None, если процесс не найден."""
    try:
        # Используем netstat для поиска PID процесса, использующего порт
        result = subprocess.check_output(f"netstat -ano | findstr :{port}", shell=True, text=True)

        # Разбираем вывод команды, чтобы найти PID процесса
        lines = result.splitlines()
        if lines:
            pid = int(lines[-1].split()[-1])  # PID - последнее значение в строке
            return pid
        return None
    except subprocess.CalledProcessError:
        # Если процесс не найден, команда netstat завершится с ошибкой
        return None


def kill_process(pid):
    """Завершает процесс с указанным PID."""
    try:
        subprocess.check_call(f"taskkill /PID {pid} /F", shell=True)
        print(f"Процесс с PID {pid} был завершен.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при завершении процесса с PID {pid}: {e}")


def start_server(port):
    """Пытается запустить сервер на указанном порту."""
    # Замените команду на ту, которая запускает ваш сервер
    try:
        subprocess.check_call(["python", "-m", "http.server", str(port)])
    except subprocess.CalledProcessError as e:
        print(f"Не удалось запустить сервер на порту {port}: {e}")
    except KeyboardInterrupt:
        print("Сервер остановлен пользователем.")


def start_server_on_port(port):
    """Пытается запустить сервер на указанном порту, освобождает порт при необходимости."""
    pid = find_process_using_port(port)

    if pid:
        print(f"Порт {port} занят процессом с PID {pid}. Завершаем процесс...")
        kill_process(pid)
        time.sleep(1)  # Небольшая пауза, чтобы процесс завершился

    print(f"Пробуем запустить сервер на порту {port}...")
    start_server(port)

print("http://127.0.0.1:5000")

# Пример использования
if __name__ == "__main__":
    port = 5000  # Укажите нужный порт
    start_server_on_port(port)



