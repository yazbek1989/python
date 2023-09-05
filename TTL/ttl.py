import pyttsx3
import PyPDF2 as pdf
import re

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 160)
engine.setProperty('voice', voices[2].id)

with open(r'TTL\habitosatomicos.pdf', 'rb') as archivo:
    lector = pdf.PdfReader(archivo)
    numpages = len(lector.pages)
    print(f"el numero de paginas del archivo es: {numpages}")
    pagina = lector.pages[5]
    pretexto = pagina.extract_text()
    
pattern = r"\n"
replacement = " "
texto = re.sub(pattern,replacement,pretexto)
print(texto)
engine.say(texto)
engine.runAndWait()