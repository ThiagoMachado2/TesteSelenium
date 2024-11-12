import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_path_with_file_name(filename: str) -> str:
    path = os.path.join("C:/Users/thiag/OneDrive/Área de Trabalho/GitHub/TesteSelenium", filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    return path

def configure_selenium() -> webdriver:
    try:
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", False)
        driver = webdriver.Chrome(service=service, options=options)
        print("ChromeDriver inicializado com sucesso.")
        driver.get(get_path_with_file_name("Login.html"))
        print("Acesso ao arquivo HTML realizado com sucesso.")
        return driver
    except Exception as e:
        print(f"Erro ao inicializar o ChromeDriver: {e}")
        raise

def test_email_is_invalid():
    # Arrange
    driver = configure_selenium()
    print("Configurando o teste para email inválido.")
    driver.find_element(By.ID, "email").send_keys("dasdasdasdasddsddsd")
    driver.find_element(By.ID, "password").send_keys("123456789")
    driver.find_element(By.ID, "phone").send_keys("(75) 55544-4444")
    driver.find_element(By.ID, "cpf").send_keys("210.830.180-19")
    driver.find_element(By.ID, "confirmPassword").send_keys("123456789")
    driver.find_element(By.ID, "signin").click()

    # Act
    print("Submetendo o formulário com email inválido.")
    driver.find_element(By.ID, "signin").click()

    # Assert
    element_message_feedback = driver.find_element(By.ID, "messageFeedback").text
    print(f"Mensagem de feedback: {element_message_feedback}")
    assert element_message_feedback == "Formato de email inválido!"
    time.sleep(5)
    driver.quit()

def test_login_must_save_successfully():
    # Arrange
    driver = configure_selenium()
    print("Configurando o teste para login bem-sucedido.")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("123456789")
    driver.find_element(By.ID, "phone").send_keys("(75) 55544-4444")
    driver.find_element(By.ID, "cpf").send_keys("210.830.180-19")
    driver.find_element(By.ID, "confirmPassword").send_keys("123456789")
    driver.find_element(By.ID, "signin").click()

    # Act
    print("Submetendo o formulário com dados corretos.")
    driver.find_element(By.ID, "signin").click()

    # Assert
    element_message_feedback = driver.find_element(By.ID, "messageFeedback").text
    print(f"Mensagem de feedback: {element_message_feedback}")
    assert element_message_feedback == "Cadastro realizado com sucesso!"
    time.sleep(5)
    driver.quit()

def test_phone_is_invalid():
    # Arrange
    driver = configure_selenium()
    print("Configurando o teste para telefone inválido.")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("123456789")
    driver.find_element(By.ID, "phone").send_keys("(75) 1234-5678")
    driver.find_element(By.ID, "cpf").send_keys("210.830.180-19")
    driver.find_element(By.ID, "confirmPassword").send_keys("123456789")
    driver.find_element(By.ID, "signin").click()

    # Act
    print("Submetendo o formulário com telefone inválido.")
    driver.find_element(By.ID, "signin").click()

    # Assert
    element_message_feedback = driver.find_element(By.ID, "messageFeedback").text
    print(f"Mensagem de feedback: {element_message_feedback}")
    assert element_message_feedback == "Formato de telefone incorreto!"
    time.sleep(5)
    driver.quit()

def test_cpf_is_invalid():
    # Arrange
    driver = configure_selenium()
    print("Configurando o teste para CPF inválido.")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("123456789")
    driver.find_element(By.ID, "phone").send_keys("(75) 55544-4444")
    driver.find_element(By.ID, "cpf").send_keys("123.456.789-00")
    driver.find_element(By.ID, "confirmPassword").send_keys("123456789")
    driver.find_element(By.ID, "signin").click()

    # Act
    print("Submetendo o formulário com CPF inválido.")
    driver.find_element(By.ID, "signin").click()

    # Assert
    element_message_feedback = driver.find_element(By.ID, "messageFeedback").text
    print(f"Mensagem de feedback: {element_message_feedback}")
    assert element_message_feedback == "CPF inválido!"
    time.sleep(5)
    driver.quit()

def test_password_min_length():
    # Arrange
    driver = configure_selenium()
    print("Configurando o teste para senha com comprimento mínimo.")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("1234567")
    driver.find_element(By.ID, "phone").send_keys("(75) 55544-4444")
    driver.find_element(By.ID, "cpf").send_keys("210.830.180-19")
    driver.find_element(By.ID, "confirmPassword").send_keys("1234567")
    driver.find_element(By.ID, "signin").click()

    # Act
    print("Submetendo o formulário com senha abaixo do mínimo.")
    driver.find_element(By.ID, "signin").click()

    # Assert
    element_message_feedback = driver.find_element(By.ID, "messageFeedback").text
    print(f"Mensagem de feedback: {element_message_feedback}")
    assert element_message_feedback == "A senha deve ter no mínimo 8 caracteres!"
    time.sleep(5)
    driver.quit()

def test_passwords_do_not_match():
    # Arrange
    driver = configure_selenium()
    print("Configurando o teste para senhas não coincidentes.")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("123456789")
    driver.find_element(By.ID, "phone").send_keys("(75) 55544-4444")
    driver.find_element(By.ID, "cpf").send_keys("210.830.180-19")
    driver.find_element(By.ID, "confirmPassword").send_keys("12345678")
    driver.find_element(By.ID, "signin").click()

    # Act
    print("Submetendo o formulário com senhas não coincidentes.")
    driver.find_element(By.ID, "signin").click()

    # Assert
    element_message_feedback = driver.find_element(By.ID, "messageFeedback").text
    print(f"Mensagem de feedback: {element_message_feedback}")
    assert element_message_feedback == "As senhas não coincidem!"
    time.sleep(5)
    driver.quit()

# Executa os testes
test_email_is_invalid()
test_login_must_save_successfully()
test_phone_is_invalid()
test_cpf_is_invalid()
test_password_min_length()
test_passwords_do_not_match()
