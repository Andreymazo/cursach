import time

def read_file_timed(file):
    """Возвращает содержимое файла и измеряет требуемое время."""
    start_time = time.time()
    try:
        f = open(file, 'rb')
        try:
            s = f.read()#Содержимое file в переменной s
            #print(s) v zadanii vrode tolko schitat nado file

        finally:
            f.close()
    except FileNotFoundError as e:
        print(e)
        print('Time required for video2.mp4 = 0.0')
    else:
        print(f'Time required for {file}: {time.time()-start_time}')

video_data = read_file_timed('video.mp4')  # 155 MB
# Time required for video.mp4 = 0.06553506851196289

# попытка считать отсутствующий файл
# >>> video_data = read_file_timed('file_not_exist.mp4')  # 155 MB
# FileNotFoundError: [Errno 2] No such file or directory: 'video2.mp4'
# Time required for video2.mp4 = 0.0
#
#
# try:
# #     file = open("myfile.txt")
# #
# #     try:
# #         s = file.readlines()
# #         print(s)
# #     finally:
# #         file.close()
# #
# # except FileNotFoundError:
# #     print("Невозможно открыть файл")