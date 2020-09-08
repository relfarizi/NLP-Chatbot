# import library
from datetime import datetime
import random

# ganti dengan sebuah nama
nama  = "Fulan"
# variabel tanggal
tanggal = datetime.now().day
# default variabel untuk pertanyaan tidak diketahui
default = "maaf, aku tidak tahu jawaban dari pertanyaanmu"

# Membuat objek dictionary berisi berbagai opsi jawaban

# list jawaban untuk pertanyaan tentang nama
jawaban_nama = [
      "nama saya  {0}".format(nama),
      "orang-orang memanggil saya {0}".format(nama),
      "panggil saja saya {0}".format(nama)
   ]

# list jawaban untuk pertanyaan tentang tanggal
jawaban_tanggal = [
      "hari ini tanggal {0}".format(tanggal),
      "ya ampun masa tidak tahu, hari ini tanggal".format(tanggal)
    ]

# opsi pertanyaan yang bisa dijawab
pertanyaan = {
  "nama kamu siapa?": jawaban_nama,
  "kamu siapa?" : jawaban_nama,
  "tanggal berapa hari ini?": jawaban_tanggal,
  "hari ini tanggal berapa?" : jawaban_tanggal,
  "default": default
}

# list jawaban untuk sebuah argument selain pertanyaan
statement =  [
                  'ceritakan lebih banyak!',
                  'kenapa kamu berpikir begitu?',
                  'sudah berapa lama kamu merasa seperti ini?',
                  'Itu sangat menarik!',
                  'oh wow!',
                  ':)'
              ]

# respon keseluruhan
responses = {
    'pertanyaan' : pertanyaan,
    'statement' : statement
}
#------
             
# ayo buat chatbotmu
def chatbot(message):
  
  if "?" in message :
    result = pertanyaan['default']
    if message in responses['pertanyaan']:
      mes = pertanyaan[message]
      result = mes[random.randint(0,len(mes)-1)]
  else :
    result = statement[random.randint(0,len(statement)-1)]
  return result

      

print(chatbot('Selamat Pagi'))
print(chatbot('Mau bermain bersamaku?'))
print(chatbot('nama kamu siapa?'))
print(chatbot('hari ini tanggal berapa?'))