# Wioniqle.q Voice Asistan

Google Asistan,Siri gibi mantığı olan sesli komut ile işlemlerinizi yaptırabileceğiniz "Sesli Asistan" uygulamasıdır.

## Ana Menü
Proje üstünde değişiklik yapabilmeniz ve eğer dilerseniz pr(pull request) atarak geliştirmeme yardımcı olabileceğiniz sesli asistan uygulamasının kodlarını veriyorum.
Kodlar benim tarafımdan yazıldı.

## Kurulum
Python'un en son versiyonunu indirin.

```sh
pip install os sys gtts speech_recognition tkinter playsound
```

## Önemli
Python'un en son versiyonunda(3.10) PlaySound **MCI** aygıt girişi hatası alabilirsiniz, bunu düzeltmek için;

```sh
pip install playsound==1.2.2
```

## Başlangıç
- Projeyi indirdikten sonra klasör içinde ``cmd`` açıp, açılan cmd ekranında ``py Index.py`` yazarak programı başlatın.
- Asistan her konuşmasını yaptıktan sonra ikinci bir komuta kadar **2 saniye** beklemeniz gerekiyor.

## İrtibat
- wioniqle.q#4661 | 790018895847096380
