from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time

class WhatsAppBot:
    def __init__(self):
        # Configuración inicial del bot
        self.working_directory = os.getcwd()  # Obtiene el directorio de trabajo actual
        self.chrome_options = Options()  # Opciones para el navegador Chrome
        self.chrome_options.add_argument(f"--user-data-dir={self.working_directory}/ChromeProfile")  # Establece el directorio de perfil de Chrome
        self.driver = Chrome(options=self.chrome_options)  # Inicializa el controlador de Chrome
        self.message_input_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]'  # XPath del área de entrada de mensaje

    def send_messages(self, contacts):
        # Iteración a través de los contactos y envío de mensajes
        for name, number in contacts:
            url = f"https://web.whatsapp.com/send?phone={number}"  # Construye la URL de WhatsApp para el contacto
            self.driver.get(url)  # Accede a la URL de WhatsApp
            time.sleep(25)  # Espera a que la página cargue completamente

            try:
                message_input_element = self.driver.find_element(By.XPATH, self.message_input_xpath)  # Busca el elemento de entrada de mensaje

                if message_input_element.is_enabled():
                    # Mensajes a enviar
                    messages = [
                        f"Hola {name}. Mi nombre es Ángel Sánchez, fundador de Azul School...",
                        "Te mando mensaje ya que estamos celebrando nuestro cuarto aniversario...",
                        "¿Te gustaría que te brinde información? Quedan pocas disponibles."
                    ]

                    for message in messages:
                        message_input_element.send_keys(message)  # Ingresa el mensaje
                        message_input_element.send_keys(Keys.RETURN)  # Presiona Enter para enviar el mensaje
                        time.sleep(3)  # Espera entre cada mensaje

                    print(f"Mensaje enviado correctamente a {name} ({number}).")

            except Exception as e:
                print(f"No se pudo encontrar el elemento para {name} ({number}). Error: {str(e)}")

            time.sleep(10)  # Espera antes de pasar al siguiente contacto

        self.driver.quit()  # Cierra el navegador al finalizar el envío de mensajes

if __name__ == "__main__":
    # Inicialización del bot y envío de mensajes a los contactos
    bot = WhatsAppBot()
    contacts = [
        ("Nombre", "521111111111"),
        # Agregar más contactos si es necesario
    ]
    bot.send_messages(contacts)