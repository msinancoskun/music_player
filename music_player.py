from tkinter import *
import pygame
from tkinter import filedialog, messagebox


class MusicPlayer(Frame):

    def __init__(self, parent):
        super(MusicPlayer, self).__init__()
        self.parent = parent
        self.playlist = []
        self.album = []
        self.songs = []
        self.start_gui()

    def start_gui(self):
        label = Label(root, text='Music Player', bg='#fff', fg='#f00', pady=10, padx=10, font=10, anchor='e')
        label.pack()

        self.playlist_box = Listbox(width=40, height=10, selectmode=SINGLE)
        for song in self.playlist:
            self.playlist_box.insert(END, song)
        self.playlist_box.pack()

        loop_button = Button(text='Loop', width=25, command=MusicPlayer.loop)
        loop_button.pack()

        play_button = Button(text='Play', width=25, command=self.play_music)
        play_button.pack()

        stop_button = Button(text='STOP', width=25, command=MusicPlayer.stop_music)
        stop_button.pack()

        choose_music_button = Button(text='What to play', width=25, command=self.choose_music)
        choose_music_button.pack()

    def play_music(self):
        if len(self.playlist) == 0:
            messagebox.showinfo('Notification', 'Nothing is in your playlist!\nClick Add to add songs.')
        else:
            pygame.mixer.music.stop()
            select_songs = self.playlist_box.curselection()
            print(select_songs)

    def stop_music(self):
        pass

    def loop(self):
        pass

    def choose_music(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

        self.songs.append(filename.split('.')[0])


if __name__ == '__main__':
    root = Tk()
    root.title('Music Player')
    # root.geometry('300x300')
    app = MusicPlayer(root)
    root.mainloop()
