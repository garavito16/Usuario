class Usuario:		# esto es lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    
    # agregando el método de depósito
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
        self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido

    # agregando el método de retiro
    def hacer_retiro(self, amount):     # toma un argumento que es el monto del retiro
        self.balance_cuenta -= amount   # la cuenta del usuario específico disminuye en la cantidad del valor recibido

    def mostrar_balance_usuario(self):
        print(f"User: {self.name}, Balance: {self.balance_cuenta}")

    def transferir_dinero(self, usuario, amount):
        self.balance_cuenta -= amount
        usuario.balance_cuenta += amount
