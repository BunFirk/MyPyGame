from Shop import Shop
from ConsoleTools import ConsoleTools
from colorama import Fore, Back, Style
consoleTools = ConsoleTools()

class Commands:
    def __init__(self):
        consoleTools.clearConsole()
        self.shop = Shop()
        self.shopList = self.shop.products
        self.run()  # Запускаем обработку команд
        self.productPriceOut = []

    def run(self):
        while True:
            self.playerInput = input("> ").strip().lower()

            match self.playerInput:
                case "shop":
                    self.shop.productList()  # Выводим список товаров
                    self.shopInput = input("> ").strip().lower()
                    self.checkBuy = False
                    self.wallet = 100
                    self.productPriceOut = self.shop.productsPrices
                    match self.shopInput:
                        case "1":
                            print("Вы точно хотите купить:")
                            print(self.shopList[0])
                            self.checkBuy = input("y/n:")
                            match self.checkBuy:
                              case "y"| "Y" | "yes" | "Yes" | "YES" :

                                      self.wallet -=  self.productPriceOut[0]
                                      print(f"Поздравляю с преобритением {self.shopList[0]}! У вас осатлось {Style.BRIGHT}{self.wallet}${Style.RESET_ALL}")
                                 
                                
                            
                            
                case "help":
                    print(f"{Style.BRIGHT}shop{Style.RESET_ALL} - Магазин")
                     
                case "exit":
                    print("Приходи ещё!")
                    break  # Выходим из цикла
                case _:
                    print("Неизвестная команда.")
                    

if __name__ == "__main__":
    c = Commands()