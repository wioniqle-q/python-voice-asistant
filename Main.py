from concurrent.futures import ThreadPoolExecutor 
import os 
import threading
import speech_recognition as sr 
from gtts import gTTS 
from playsound import playsound 
from tkinter import *
import sys 

class AudioService: 
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.pause_threshold = 0.8 

    def audioAsistant(self): 
        with sr.Microphone() as source: 
            audio = self.recognizer.listen(source) 

        try: 
            query = self.recognizer.recognize_google(audio, language='tr-TR') 
            print(f"Konuşan Kullanıcı: {query}\n") 
        except Exception as e: 
            self.audioAsistant() 
            return "None" 
        return query 

    def speakAudio(self, text): 
        translate_file = gTTS(text=text, lang='tr') 
        filename = 'translated.mp3' 
        translate_file.save(filename) 
        playsound("translated.mp3") 
        os.remove(filename) 

    def close(self):
        os._exit(0)

    def digitalAsistan(self): 
        self.speakAudio("merhaba ben kişisel asistanınızım") 
        self.speakAudio("adım kent Size nasıl yardımcı olabilirim") 
        
        while True: 
            getQuery = self.audioAsistant() 
            
            if getQuery == "None":
                continue 
            
            elif 'merhaba' in str(getQuery).lower(): 
                self.speakAudio("Merhaba efendim!")

            elif 'çıkış' in str(getQuery).lower(): 
                self.speakAudio("Görüşürüz")
                self.close() 
                
class TkinterGUI: 
    def __init__(self): 
        self.root = Tk() 
        self.root.title("Python Voice Asistant")
        self.root.geometry("300x320+500+500") 
        self.root.resizable(False, False) 
        self.root.configure(background='#f2f2f2') 
        self.root.protocol("WM_DELETE_WINDOW", self.close) 
        self.frameCnt = 12 
        self.frames = [PhotoImage(file=self.get_file(),format = 'gif -index %i' %(i)) for i in range(self.frameCnt)] 
        
        self.label = Label(self.root) 
        self.label.pack() 
        self.root.after(0, self.play_gif, 0) 

        self.root.mainloop() 

    def play_gif(self, index): 
        frame = self.frames[index]  
        index += 1 
        if index == self.frameCnt: 
            index = 0 # 
            self.label.configure(image=self.frames[0])
        else: 
            self.label.configure(image=frame) 
        self.root.after(100, self.play_gif, index) 

    def canvas(self): 
        self.canvas = Canvas(self.root, width=300, height=300)
        self.canvas.pack() 
        self.canvas.create_image(0, 0, image=self.frames[0], anchor=NW) 
        self.root.after(0, self.play_gif, 0) 
        self.root.mainloop() 

    def close(self): 
        self.root.destroy() 
        sys.exit() 
        
    def get_file(self):
        for root, dirs, files in os.walk(os.getcwd()): 
            for file in files: 
                if file.endswith(".gif"): 
                    return os.path.join(root, file) 
        
if __name__ == "__main__": 
    thread = threading.Thread(target=TkinterGUI) 
    thread.start() 
    
    audioService = threading.Thread(target=AudioService().digitalAsistan) 
    audioService.start() 
