import pyautogui
import time
import random
import keyboard
import winsound

# Cor que você deseja detectar (RGB)
target_color = (75, 219, 106)
active = True

# Função para ativar/desativar o programa
def toggle_program():
    global active
    active = not active
    if active:
        print("Programa ativado. Use 'Ctrl+Alt+P' para desativar.")
        winsound.Beep(1000, 200)
    else:
        print("Programa desativado. Use 'Ctrl+Alt+P' para ativar.")
        winsound.Beep(500, 200)

# Registra a tecla de atalho 'Ctrl+Alt+P' para ativar/desativar o programa
keyboard.add_hotkey('ctrl+alt+p', toggle_program)

# Banner informativo personalizado
banner = """
*************************************************
*                                              *
*  Programa para Reaction Time do Benchmark    *
*                                              *
*  Autor: @nicolaspoersch (GitHub)             *
*                                              *
*  Programa ativado. Use 'Ctrl+Alt+P' para     *
*  desativar.                                  *
*                                              *
*************************************************
"""

print(banner)

while True:
    if active:
        x, y = pyautogui.position()
        pixel_color = pyautogui.pixel(x, y)

        if pixel_color == target_color:
            delay = random.uniform(0.15, 0.16)
            time.sleep(delay)
            pyautogui.click(x, y)
