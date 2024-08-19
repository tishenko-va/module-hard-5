import hashlib
import time

class User:
      def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

      def hash(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

      def __str__(self):
        return f"{self.nickname}"
# Атриубуты: title(заголовок, строка), duration(продолжительность,
# секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
class Video:
    def __init__(self, title: str, duration: int, time_now: int, adult_mode: bool=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        print(f'Название видео:{self.title}')

class UrTube:
    # Атриубты: users(список объектов User), videos(список
    # объектов Video), current_user(текущий пользователь, Use
    def __init__(self, users: list[User], videos: [Video], current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user
# Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users
# с такими же логином и паролем.
# Если такой пользователь существует, то current_user меняется на найденного.
# Помните, что password передаётся в виде строки, а сравнивается по хэшу.
    def log_in(self, nickname, password):

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Пользователь {nickname} вошёл в систему.")
                return True
# Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
# если пользователя не существует (с таким же nickname).
# Если существует, выводит на экран: "Пользователь {nickname} уже существует".
    def register(self, nickname, password, age):
        new_user = []
        for nickname in new_user:
            if nickname in new_user:
                print('Пользователь с таким ником уже существует')
            else:
                new_user.append(list[nickname, password, age])

    def log_out(self):
        self.current_user = None


# Метод add, который принимает неограниченное кол - во объектов
# класса Video и все добавляет в videos, если с таким же названием видео ещё не
# существует.В противном случае ничего не происходит.
    def add(self, *video: list[Video]):
        videos = []
        for video in videos:
            if video not in videos:
                videos.append(video)
            else:
                return

# get_videos, который принимает поисковое слово и возвращает список названий всех видео,
# содержащих поисковое слово.Следует учесть, что слово'UrbaN'присутствует в строке'Urban the
    # best'(не учитывать регистр)
    def get_videos(self, find_word):
            find_word_lower = find_word.lower()
            for find_word_lower in self.videos:
                if find_word_lower in self.videos.title.lower:
                    return {self.videos.title}

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for title in self.videos:
                if title == self.videos.title:
                    if video.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        return
                    for i in range(video.time_now, video.duration + 1):
                        print(i, end=' ')
                        video.time_now = 0
                        return
            print('Конец  видео')

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200, 0, True)
    v2 = Video('Для чего девушкам парень программист?', 10, 0, adult_mode=True)

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

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')