# -*- coding:utf-8 -*-
# By Mak4ic
# Если есть какие-то вопросы напишите мне: https://vk.com/mak4ic
# Для получение access_token
# За место %appid% впишите свой id от приложение которое вы создали.
# https://oauth.vk.com/authorize?client_id=%appid%&display=page&scope=status,friends&response_type=token&v=5.92&state=123456


import vk_api
import datetime # работа с датой и временем
import time
import requests

while True:
	vk = vk_api.VkApi(token="Впишите свой токен")
	# Впишите в hours= например +3 для Москвы или +5 Екатеринбурга.
	delta = datetime.timedelta(hours=3, minutes=0)
	t = (datetime.datetime.now(datetime.timezone.utc) + delta) # Присваиваем дату и время переменной «t»
	nowtime = t.strftime("%H:%M") # текущее время
	nowdate = t.strftime("%d.%m.%Y") # текущая дата

	on = vk.method("friends.getOnline") # получаем список id друзей онлайн
	counted = len(on) # считаем кол-во элементов в списке
	if counted >= 10:
		print(" ● OwO" + " ● " + "Друзей онлайн: " + str(counted) + " ● " + nowtime + " ● " + nowdate + " ● ")
		vk.method("status.set", {"text": " ● OwO" + " ● " + "Друзей онлайн: " + str(counted) + " ● " + nowtime + " ● " + nowdate + " ● "})
	else:
		print(" ● UwU" + " ● " + "Друзей онлайн: " + str(counted) + " ● " + nowtime + " ● " + nowdate + " ● ")
		vk.method("status.set", {"text": " ● UwU" + " ● " + "Друзей онлайн: " + str(counted) + " ● " + nowtime + " ● " + nowdate + " ● "})
	print("Sleep...zzZ")
	time.sleep(60) # погружаем скрипт в «сон» на 60 секунд
