import time
from typing import List


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return hash(self.password)


    def __str__(self):
        return (f"{self.nickname} {self.password} {self.age}")


class Video:
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, title: str, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return (f"{self.title} {self.time_now} {self.duration} {self.adult_mode}")


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname, password, age):

        for user in self.users:
            if nickname in user.nickname:
                print(f"уже {nickname} есть")
                break

        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_in(user.nickname, user.password)


    def log_out(self):
        self.current_user = None

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title  == title and self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста, покиньте страницу')
            for i in range(video.duration):
                print(i, end=' ')
                video.time_now += 1
            print("Конец видео")

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, word):
        list_video = []
        for i in self.videos:
            if word.casefold() in i.title.casefold():
                list_video.append(i.title)
        return list_video

    def __str__(self):
        return (f"{self.videos} {self.users} {self.current_user}")




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
