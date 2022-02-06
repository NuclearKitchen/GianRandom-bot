import os
import discord
import random
from replit import db

client  = discord.Client()

def update_risposta(offesa):
  if "risposta" in db.keys():
    risposta = db["risposta"]
    risposta.append(offesa)
    db["risposta"] = risposta
  else:
    db["risposta"] = [offesa]

def cancella_risposta(index):
  risposta = db["risposta"]
  if len("risposta") > index:
    del risposta[index]
    db["rispotsa"] = risposta


parole_trigger = ["Giornata rovinata", "Noob", "Ez","Gianni","Negro",
"giornata rovinata", "noob", "ez", "gianni", "negro", "coglione", "Coglione", "Frocio", "frocio"]

if "rispondere" not in db.keys():
  db["rispondere"] = True

risposta_iniziale = ["Non mi sembra appropriato il tuo comportamento",
"Vaffanculo", "Pezzo di merda"]

@client.event
async def on_ready():
  print("Sono loggato come {0.user}.format(client)")

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    msg = message.content

    if msg.startswith("-Saluto"):
      await message.channel.send("Sono tornato merde")

    if message.content.startswith("-help"):
      await message.channel.send("Coglionazzo, i miei comandi sono:\n"
      "- = Prefisso generico, tipo groovy ma peggio\n"
      "-Saluto = Un saluto\n"
      "-help = questa lista\n"
      "-aggiungi_risposta = aggiunge una risposta a quelle già conosciute \n"
      "-cancella_risposta = cancella una risposta dalla lista\n"
      "-lista_risposte = lista di tutte le risposte\n"
      "-rispondere (""rispondere (attivo/disattiva) = indica se devo rispondere a ciò che scrivi o meno")

    if db["rispondere"]:
      opzioni = risposta_iniziale
      if "risposta" in db.keys():
        opzioni = opzioni + db["risposta"].value

      if any(word in msg for word in parole_trigger):
        await message.channel.send(random.choice(opzioni))

    if msg.startswith("-aggiungi_risposta"):
      offesa = msg.split("-aggiungi_risposta ", 1)[1]
      update_risposta(offesa)
      await message.channel.send("Nuova risposta aggiunta")

    if msg.startswith("-cancella_risposta"):
      risposta = []
      if "risposta" in db.keys():
        index = int(msg.split("-cancella_risposta ", 1)[1])
        cancella_risposta(index)
        risposta = db["risposta"]
        await message.channel.send(risposta)

    if msg.startswith("-lista_risposte"):
      risposta = []
      if "risposta" in db.keys():
        risposta = db["risposta"]
      await message.channel.send(risposta)

    if msg.startswith("-rispondere"):
      value = msg.split("-rispondere ",1)[1]

      if value.lower() == "attiva":
        db["rispondere"] = True
        await message.channel.send("Ora posso rispondere")

      if value.lower() == "disattiva":
        db["rispondere"] == False
        await message.channel.send("Mi hai mutato. Giornata Rovinata")
client.run(os.getenv("TOKEN"))

