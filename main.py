#If on Windows to avoid fullscreen, use the following two lines of code
from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.uix.togglebutton import ToggleButton

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
        pos_hint:{'center_x':.5, 'center_y':.5}
        GridLayout:
            id: scroll
            cols: 1
            spacing: 10
            size_hint_y: None

    GridLayout:
        rows: 1
        size: root.width, 50
        Button:
            id: nowplay
            background_color: 0,.5,1,1
        Button:
            text: '<='
            background_color: 0,.5,1,1
        Button:
            text: '[ ]'
            background_color: 0,.5,1,1
        Button:
            text: '=>'
            background_color: 0,.5,1,1
            

''')

class MusicPlayer(Widget):

    def getSongs(self):

        songs = [] #List to hold songs from music directory
        directory = self.ids.direct.text #Directory entered by the user

        self.ids.scroll.bind(minimum_height=self.ids.scroll.setter('height'))

        #get mp3 files from directory
        for fil in listdir(directory):
            if fil.endswith('.mp3'):
                songs.append(directory+fil)
                
        songs.sort()

        for song in songs:

            def playSong(self):
                sound = SoundLoader.load(directory+self.text)
                if self.state == 'down':
                    sound.play()
                else:
                    sound.stop()
                
            news = song.replace(directory,'') #song name
            btn = ToggleButton(text=news, size_hint_y=None, height=40)
            btn.bind(on_press=playSong)

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
