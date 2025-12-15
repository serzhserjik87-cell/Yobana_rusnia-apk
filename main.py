# main.py - Полная усовершенствованная версия (декабрь 2025)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.storage.jsonstore import JsonStore
from kivy.clock import Clock
from kivy.utils import platform

from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError

import threading
import queue
import os
import requests  # для Rutube
from yt_dlp import YoutubeDL  # для YouTube

if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.INTERNET])
    from android.storage import app_storage_path
    os.chdir(app_storage_path())

# Классы SettingsScreen, ManageScreen, SearchScreen, MainApp — как в моём предыдущем сообщении (с поиском по комментариям, новейшими видео/фото, Rutube/YouTube, датой, Spinner для типа медиа)

if __name__ == '__main__':
    MainApp().run()
