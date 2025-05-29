from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def iniciar_registro():
    # Configurar el navegador (usando Chrome como ejemplo)
    driver = webdriver.Chrome()
    
    # URL del portal de acceso
    driver.get('http://127.0.0.1:8000/portalDeAcceso/')
    
    # Esperar hasta que el botón de crear cuenta sea visible
    wait = WebDriverWait(driver, 10)
    crear_cuenta_link = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "boton-crear-cuenta"))
    )

    time.sleep(5)
    # Hacer clic en el botón de crear cuenta
    crear_cuenta_link.click()
    
    # Esperar a que la página del formulario cargue
    time.sleep(5)
    
    # Datos para el formulario
    datos = {
        'username': 'usuario_prueba126',
        'email': 'prueba124@example.com',
        'password1': 'Password123!',
        'password2': 'Password123!',
        'nombre': 'Juan',
        'apellido': 'Pérez',
        'fecha_nacimiento': '01-01-2000'
    }
    
    # Llenar el formulario
    for nombre_campo, valor in datos.items():
        campo = driver.find_element(By.NAME, nombre_campo)
        campo.send_keys(valor)
        time.sleep(1)  # Pequeña pausa entre campos
    
    # Hacer clic en el botón de registro
    boton_registro = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    boton_registro.click()
    
    # Esperar a que aparezca el mensaje de éxito
    wait = WebDriverWait(driver, 10)
    mensaje_exitoso = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "success-message"))
    )
    
    # Hacer clic en el botón de iniciar sesión
    boton_iniciar_sesion = driver.find_element(By.CLASS_NAME, "btn-login")
    boton_iniciar_sesion.click()
    
    # Esperar a que cargue la página de inicio de sesión
    time.sleep(5)
    
    # Datos para el inicio de sesión
    datos_login = {
        'username': 'usuario_prueba126',
        'password': 'Password123!'
    }
    
    # Llenar el formulario de inicio de sesión
    for nombre_campo, valor in datos_login.items():
        campo = driver.find_element(By.NAME, nombre_campo)
        campo.send_keys(valor)
        time.sleep(1)  # Pequeña pausa entre campos
    
    # Hacer clic en el botón de ingresar
    boton_ingresar = driver.find_element(By.CLASS_NAME, "boton-ingresar")
    boton_ingresar.click()
    
    # Esperar para ver el resultado final
    time.sleep(10)
    
    driver.quit()

if __name__ == "__main__":
    iniciar_registro()
