from Usuario import Usuario

adrien = Usuario("Adrien","adrien.85@hotmail.com")
nibbles = Usuario("Mr. Nibbles","nibbles2088@hotmail.com")
benny = Usuario("Benny Bob","benny2022@outlook.com")

adrien.hacer_depósito(100)
adrien.hacer_depósito(100)
adrien.hacer_depósito(200)
adrien.hacer_retiro(95)
adrien.mostrar_balance_usuario()

nibbles.hacer_depósito(1000)
nibbles.hacer_depósito(1000)
nibbles.hacer_retiro(400)
nibbles.hacer_retiro(400)
nibbles.mostrar_balance_usuario()

benny.hacer_depósito(1000)
benny.hacer_retiro(4000)
benny.hacer_retiro(4000)
benny.hacer_retiro(500)
benny.mostrar_balance_usuario()

nibbles.transferir_dinero(adrien,400)
nibbles.mostrar_balance_usuario()
adrien.mostrar_balance_usuario()