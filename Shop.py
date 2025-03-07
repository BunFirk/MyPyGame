from colorama import Fore, Back, Style
import random
import os
from ConsoleTools import ConsoleTools

consoleTools = ConsoleTools()

class Shop:
    def __init__(self):
        self.shopLevel = 1
        self.priceMultiplier = random.randint(1, 5)
        self.productsName = ["Меч", "Броня", "Кольцо", "Ботинки", "Ожерелье"]
        self.productEffects = {
        "swordEffects" : [
        f"{Fore.BLUE + Style.BRIGHT}Олядинение{Style.RESET_ALL}", 
        f"{Fore.RED}Огненный клинок{Style.RESET_ALL}", 
        f"{Fore.BLUE + Style.BRIGHT}Пробитие{Style.RESET_ALL}", 
        f"{Fore.GREEN + Style.BRIGHT}Лёгкость{Style.RESET_ALL}", 
        f"{Fore.RED + Style.BRIGHT}Тяжесть{Style.RESET_ALL}", 
        f"{Fore.RED + Style.BRIGHT}Затупленость{Style.RESET_ALL}"]}
        effectApply = []
        self.products = []
        self. productsPrices = []
        self.weaponRarity = [1, 2, 3, 4, 5]
        self.productsPrice = 0
        
    def generateShop(self):
        self.products.clear()
        for i in range(1, 6):
            self.productsPrice = self.priceMultiplier + random.randint(0, self.shopLevel + 3)
            effectsApply = random.choice(self.productEffects['swordEffects'
            ])
            self.products.append(f"{i}. {Style.BRIGHT}{self.productsName[0]}{Style.RESET_ALL} -> {effectsApply} (${self.productsPrice})")
        
    def productList(self):
        consoleTools.clearConsole()
        self.generateShop()
        print(" ")
        print(Style.BRIGHT + f"Магазин lv. {Fore.GREEN}{self.shopLevel}{Style.RESET_ALL}" + Style.RESET_ALL)
        print("-------")
        for product in self.products:
            print(product)
            

        
        

a = Shop()
a.productList()