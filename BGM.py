import PySimpleGUI as pg
import playsound, multiprocessing, sys

"""def delete(object):
    del object"""
def play(filepath):
    while True:
        playsound.playsound(filepath)
if __name__ == "__main__":
    pg.set_options(font=(None, 24))
    with open("bgmpath.txt", "r", encoding="utf-8") as f:
        bgmfilepath = f.read()
    class sound:
        def __init__(self):
            """with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                executor.submit(playsound.playsound, "BGM.mp3")
            #playsound.playsound("BGM.mp3")"""
            self.p = multiprocessing.Process(target=play, args=(bgmfilepath,))
            self.p.start()
            #p.join()
            #sound()
        def stop(self):
            self.p.terminate()
    layout = [
        [pg.Input(bgmfilepath, k="bgmpath", enable_events=True),
          pg.FileBrowse("ref...", file_types=(("audio files", "*.mp3;*.wav"), ("all files", "*")))],
        [pg.Button("start", key="start"), pg.Button("stop", key="stop")]
    ]
    player = None
    win = pg.Window("BGM", layout=layout)
    while True:
        e, v = win.read()
        #bgmfilepath = v["bgmpath"]
        if e == None: break
        if e == "start":
            if not isinstance(player, sound):
                player = sound()
                """with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                    process = executor.submit(sound, None)
            p = multiprocessing.Process(target=sound)
            p.start()
            processs.append(p)"""
        if e == "stop":
            if player:
                player.stop()
                player = None
        if e == "bgmpath":
            bgmfilepath = v["bgmpath"]
            with open("bgmpath.txt", "w", encoding="utf-8") as f:
                f.write(bgmfilepath)
    win.close()
    player.stop()