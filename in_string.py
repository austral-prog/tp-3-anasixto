def check_vowels():
    # Código a implementar utilizando input.
    
    # Input
    my_name = input()

    # Imprime en pantalla
    print("Contiene a: " + str("a" in my_name.lower()))
    print("Contiene e: " + str("e" in my_name.lower()))
    print("Contiene i: " + str("i" in my_name.lower()))
    print("Contiene o: " + str("o" in my_name.lower()))
    print("Contiene u: " + str("u" in my_name.lower()))
    
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
