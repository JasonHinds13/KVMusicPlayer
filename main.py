#If on Windows to avoid fullscreen, use the following two lines of code
from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader

from os import listdir

Builder.load_string('''
<MusicPlayer>:
    
    TextInput:
        id: direct
        pos: 0,root.top-50
        size: root.width-200,50
        hint_text: 'Enter File Location'
    Button:
        text: 'Scan'
        size: 200,50
        background_color: 0,.5,1,1
        pos: root.width-200, root.top-50
        on_release: root.getSongs()

    ScrollView:
        size_hint: None, None
        size: root.width, root.height-50
        pos_hint:{'center_x':.1, 'center_y':.1}
        GridLayout:
            id: scroll
            cols: 1
            spacing: 10
            size_hint_y: None

    GridLayout:
        rows: 1
        pos: 0, 50
        size: root.width, 50
        Button:
            text: '<='
            background_color: 0,.5,1,1
        Button:
            text: '||'
            background_color: 0,.5,1,1
        Button:
            text: '=>'
            background_color: 0,.5,1,1
    Button:
        id: nowplay
        text: ''
        pos: 0,0
        size: root.width, 50
        background_color: 0,.5,1,1
            

''')

class MusicPlayer(Widget):

    def getSongs(self):

        songs = [] #List to hold songs from music directory
        nowPlaying = '' #Song that is currently playing
        directory = self.ids.direct.text #Directory entered by the user

        #To make sure that the directory ends with a '/'
        if not directory.endswith('/'):
            directory += '/'

        self.ids.scroll.bind(minimum_height=self.ids.scroll.setter('height'))

        #get mp3 files from directory
        for fil in listdir(directory):
            if fil.endswith('.mp3'):
                songs.append(fil)
                
        songs.sort()

        for song in songs:

            def playSong(bt):
                try:
                    nowPlaying.stop()
                except:
                    pass
                finally:
                    nowPlaying = SoundLoader.load(directory+bt.text)
                    #nowPlaying.play()
                    self.ids.nowplay.text = bt.text
                
            btn = Button(text=song, size_hint_y=None, height=40, on_press=playSong)

            #Color Buttons Alternatively
            if songs.index(song)%2 == 0:
                btn.background_color=(0,0,1,1)
            else:
                btn.background_color=(0,0,2,1)
                
            self.ids.scroll.add_widget(btn) #Add each to scrollview
    
class KVMusicApp(App):
    
    def build(self):
        return MusicPlayer()
        
    def on_pause(self):
        return True
        
    def on_resume(self):
        pass
        
if __name__ == "__main__":
    KVMusicApp().run()
