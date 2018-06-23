# -*- coding: utf-8 -*-
print("\n")
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot ("Test")

convA = ["oi", "ois", "eae cara", "eae cara, blz?","blz?","olá", "olá, bom dia", "bom dia", "bom dia como vai?", "estou bem"]

convB = ["que filmes voce gosta?", "eu gosto de piratas do caribe", "eu gosto de exterminador do futuro", "eu gosto de senhor dos aneis"]

convC = ["como vai você?", "vou bem", "o que esta fazendo?"]

convD = ["não interessa", "por que quer saber?"]

convE = ["você esta bem?", "sim, muito", "não, estou triste", "por que?", "por que está triste?", "por que ta triste?", "pq ta triste?", "pois você está longe de mim", "porque sim", "nao interessa", "pq qr saber?", "por que quer saber?"]

convF = ["gosto de você", "eu tambem", "eu te amo", "eu não", "eca", "não ligo"]

convG = ["o que gosta de fazer?", "jogar", "trabalhar", "programar", "brincar"]

convH = ["você gosta de jogar?","vc gosta de jogar?", "vc ta gostando da copa?", "sim", "não", "você gosta?", "que jogos voce gosta?", "Watch Dogs", "GTA", "Skyrim", "Fallout", "EU AMO ZELDA", "o protagonista de zelda é o zelda n é?", "ELE É O LINK!!!"]


bot.set_trainer(ListTrainer)

bot.train(convA)
bot.train(convB)
bot.train(convC)
bot.train(convD)
bot.train(convF)
bot.train(convG)
bot.train(convH)

while True:
	quest = input ("Você: ")

	response = bot.get_response (quest)

	print("Bot: ", response)