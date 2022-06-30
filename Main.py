from concurrent.futures import ThreadPoolExecutor # Thread modülümüzü import ediyoruz.
import os # Os modülümüzü import ediyoruz.
import threading
import speech_recognition as sr  # Speech Recognition modülümüzü import ediyoruz.
from gtts import gTTS  # Google Text to Speech modülümüzü import ediyoruz.
from playsound import playsound # Play Sound modülümüzü import ediyoruz.
from tkinter import * # Tkinter modülümüzü import ediyoruz.
import sys # Sistem modülümüzü import ediyoruz.

class AudioService: # AudioService classımız 
    def __init__(self): # AudioService classımızın constructorı
        self.recognizer = sr.Recognizer() # recognizer nesnesi oluşturduk
        self.recognizer.pause_threshold = 0.8 # recognizer nesnesinin pause_threshold değerini ayarladık

    def audioAsistant(self): # audioAsistant fonksiyonu
        with sr.Microphone() as source: # Microphone nesnesi oluşturduk
            audio = self.recognizer.listen(source) # recognizer nesnesinin listen fonksiyonu ile ses kaynağını alıyoruz

        try: # try except bloğu
            query = self.recognizer.recognize_google(audio, language='tr-TR') # recognizer nesnesinin recognize_google fonksiyonu ile ses kaynağını alıyoruz
            print(f"Konuşan Kullanıcı: {query}\n") # konuşan kullanıcının sesini yazdırıyoruz
        except Exception as e: # eğer hata varsa
            self.audioAsistant() # audioAsistant fonksiyonu ile tekrar çalıştırıyoruz
            return "None" # None döndürüyoruz
        return query # query döndürüyoruz

    def speakAudio(self, text): # speakAudio fonksiyonu
        translate_file = gTTS(text=text, lang='tr') # gTTS fonksiyonu ile text değerini türkçe yapıyoruz
        filename = 'translated.mp3' # filename değişkeni oluşturuyoruz
        translate_file.save(filename) # translate_file değişkeni içindeki değeri filename değişkeni içinde kaydediyoruz
        playsound("translated.mp3") # playsound fonksiyonu ile filename değişkeni içindeki değeri çalıyoruz
        os.remove(filename) # filename değişkeni içindeki değeri siliyoruz

    def close(self): # close fonksiyonu
        os._exit(0) # os kütüphanesinin system.exit fonksiyonu ile çalıştırıyoruz ve programı kapatıyoruz.

    def digitalAsistan(self): # digitalAsistan fonksiyonu
        self.speakAudio("merhaba ben kişisel asistanınızım") # merhaba ben kişisel asistanınızım
        self.speakAudio("adım kent Size nasıl yardımcı olabilirim") # adım kent Size nasıl yardımcı olabilirim
        
        while True: # while döngüsü
            getQuery = self.audioAsistant() # getQuery değişkeni oluşturuyoruz
            
            if getQuery == "None": # eğer getQuery değeri None ise
                continue # devam ediyoruz
            
            elif 'merhaba' in str(getQuery).lower(): # eğer getQuery değeri merhaba ise
                self.speakAudio("Merhaba efendim!") # Merhaba efendim! yazdırıyoruz

            elif 'çıkış' in str(getQuery).lower(): # eğer getQuery değeri çıkış ise
                self.speakAudio("Görüşürüz") # Görüşürüz yazdırıyoruz
                self.close() # close fonksiyonu ile programı kapatıyoruz
                
class TkinterGUI: # TkinterGUI classımız
    def __init__(self): # TkinterGUI classımızın constructorı
        self.root = Tk() # root değişkeni oluşturuyoruz
        self.root.title("Python Voice Asistant") # title değişkeni oluşturuyoruz
        self.root.geometry("300x320+500+500") # geometry değişkeni oluşturuyoruz
        self.root.resizable(False, False) # resizable değişkeni oluşturuyoruz
        self.root.configure(background='#f2f2f2') # background değişkeni oluşturuyoruz
        self.root.protocol("WM_DELETE_WINDOW", self.close) # protocol değişkeni oluşturuyoruz
        self.frameCnt = 12 # frameCnt değişkeni oluşturuyoruz
        self.frames = [PhotoImage(file=self.get_file(),format = 'gif -index %i' %(i)) for i in range(self.frameCnt)] # frames değişkeni oluşturuyoruz
        
        self.label = Label(self.root) # label değişkeni oluşturuyoruz
        self.label.pack() # label değişkeni içindeki değeri pack fonksiyonu ile yerleştiriyoruz
        self.root.after(0, self.play_gif, 0) # root değişkeni içindeki değeri play_gif fonksiyonu ile çalıştırıyoruz

        self.root.mainloop() # mainloop fonksiyonu ile root değişkeni içindeki değeri çalıştırıyoruz

    def play_gif(self, index): # play_gif fonksiyonu
        frame = self.frames[index]  # frame değişkeni oluşturuyoruz
        index += 1 # index değişkeni içindeki değeri 1 artıyoruz
        if index == self.frameCnt: # eğer index değişkeni içindeki değer self.frameCnt değerine eşit ise
            index = 0 # index değişkeni içindeki değeri 0 yapıyoruz
            self.label.configure(image=self.frames[0]) # label değişkeni içindeki değeri self.frames değişkeni içindeki değeri yerleştiriyoruz
        else: # eğer index değişkeni içindeki değer self.frameCnt değerine eşit değil ise
            self.label.configure(image=frame) # label değişkeni içindeki değeri frame değişkeni içindeki değeri yerleştiriyoruz
        self.root.after(100, self.play_gif, index) # root değişkeni içindeki değeri play_gif fonksiyonu ile çalıştırıyoruz

    def canvas(self): # canvas fonksiyonu
        self.canvas = Canvas(self.root, width=300, height=300) # canvas değişkeni oluşturuyoruz
        self.canvas.pack() # canvas değişkeni içindeki değeri pack fonksiyonu ile yerleştiriyoruz
        self.canvas.create_image(0, 0, image=self.frames[0], anchor=NW) # canvas değişkeni içindeki değeri create_image fonksiyonu ile yerleştiriyoruz
        self.root.after(0, self.play_gif, 0) # root değişkeni içindeki değeri play_gif fonksiyonu ile çalıştırıyoruz
        self.root.mainloop() # mainloop fonksiyonu ile root değişkeni içindeki değeri çalıştırıyoruz

    def close(self): # close fonksiyonu
        self.root.destroy() # root değişkeni içindeki değeri destroy fonksiyonu ile kapatıyoruz
        sys.exit() # sys.exit fonksiyonu ile programı kapatıyoruz
        
    def get_file(self): # get_file fonksiyonu
        for root, dirs, files in os.walk(os.getcwd()): # os.walk fonksiyonu ile os.getcwd() değişkeni içindeki değeri döngüye sokuyoruz
            for file in files: # files değişkeni içindeki değerleri döngüye sokuyoruz
                if file.endswith(".gif"): # eğer file değişkeni içindeki değer .gif uzantılı ise
                    return os.path.join(root, file) # os.path.join fonksiyonu ile root değişkeni içindeki değeri file değişkeni içindeki değeri yerleştiriyoruz
        
if __name__ == "__main__": # __main__ değişkeni oluşturuyoruz
    thread = threading.Thread(target=TkinterGUI) # thread değişkeni oluşturuyoruz
    thread.start() # thread değişkeni içindeki değeri start fonksiyonu ile çalıştırıyoruz
    
    audioService = threading.Thread(target=AudioService().digitalAsistan) # audioService değişkeni oluşturuyoruz
    audioService.start() # audioService değişkeni içindeki değeri start fonksiyonu ile çalıştırıyoruz

# Made by Wioniqle.q