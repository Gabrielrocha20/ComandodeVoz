import speech_recognition as sr
import pyautogui as pg
import pyperclip as pc

'''rec = sr.Recognizer()
pg.PAUSE = 1

loop = True
with sr.Microphone() as mic:
    while loop:
        rec.adjust_for_ambient_noise(mic)
        print('Pode falar')
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language='pt-BR')
        print(texto)
        if ('Parar'in texto) or ('parar' in texto):
            loop = False
        elif ('Abrir' in texto) or ('abrir' in texto):
            print(texto.replace('abrir', '').replace('Abrir', ''))
            pg.press('win')
            pg.write(texto[6:])
            pg.press('enter')'''

class Pytana:
    def __init__(self):
        self.rec = sr.Recognizer()
        self.pg = pg
        self.pc = pc

        self.pg.PAUSE = 1
        self.robo_ligado = False
        if not self.robo_ligado:
            self.desligado()

    def ouvindo(self):
        with sr.Microphone() as self.mic:
            while True:
                try:
                    self.rec.adjust_for_ambient_noise(self.mic)
                    audio = self.rec.listen(self.mic)
                    texto = self.rec.recognize_google(audio, language='pt-BR')
                    print('se falou passou, se nao bugou', texto)
                    return texto.lower()
                except sr.UnknownValueError as error:
                    print('nao falou nada')
                    continue

    def desligado(self):
        print('desligado')
        while True:
            texto = self.ouvindo()
            texto = texto.lower()
            ligar_robo = False if texto.find('robô ligar') == -1 else True

            if ligar_robo:
                self.robo_ligado = True
                return self.ligar()

            '''elif tipo == 'executar':
                if 'robô parar' in texto:
                    self.pg.press('esc')
                    return
                elif 'robô abrir' in texto:
                    texto = texto.split('robô abrir')[1]
                    print(texto)
                    return self.abrir_comando(texto)
                elif 'robô fechar' in texto:
                    return self.fechar_janela()
    
            elif tipo == 'acessar':
                return self.acessar_link(texto)'''

    def ligar(self):
        self.pg.press('win')
        self.pc.copy('Opá Chamou?')
        self.pg.hotkey('ctrl', 'v')
        return self.robo_executar()

    def robo_executar(self):
        while True:
            texto = self.ouvindo()
            ligar_robo = False if texto.find('robô ligar') == -1 else True
            if 'robô parar' in texto:
                self.pg.press('esc')
                return
            elif 'robô abrir' in texto:
                texto = texto.split('robô abrir')[1]
                print(texto)
                return self.abrir_comando(texto)
            elif 'robô fechar' in texto:
                return self.fechar_janela()

    def robo_acessar(self):
        while True:
            texto = self.ouvindo()
            return self.acessar_link(texto)

    def abrir_comando(self, texto):
        texto = texto.replace('abrir', '').replace('Abrir', '').strip().capitalize()
        self.pg.press('esc')
        self.pg.press('win')
        self.pg.write(texto)
        self.pg.press('enter')
        if ('Google' in texto) or ('Opera' in texto):
            return self.robo_acessar()

        return self.robo_executar()

    def acessar_link(self, texto):
        if ('modo 2' in texto) or ('modo dois' in texto):

        self.pc.copy(texto)
        self.pg.hotkey('ctrl', 'v')
        self.pg.press('enter')
        return self.robo_executar()

    def fechar_janela(self):
        self.pg.hotkey('alt', 'f4')
        return self.robo_executar()

teste = Pytana()
