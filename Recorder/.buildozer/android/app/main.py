from kivy.app import App
from kivy.core.text import LabelBase
from jnius import autoclass
from kivy.logger import Logger
from kivy.properties import ObjectProperty

Environment = autoclass('android.os.Environment')
MediaRecorder = autoclass('android.media.MediaRecorder')
AudioSource = autoclass('android.media.MediaRecorder$AudioSource')
OutputFormat = autoclass('android.media.MediaRecorder$OutputFormat')
AudioEncoder = autoclass('android.media.MediaRecorder$AudioEncoder')
MediaPlayer = autoclass('android.media.MediaPlayer')
File = autoclass('java.io.File')

player = MediaPlayer()
recorder = MediaRecorder()

storage_path = (Environment.getExternalStorageDirectory()
.getAbsolutePath() + '/kivy_recording.3gp')
Logger.info('App: storage path == {}'.format(storage_path))

def init_recorder():
    recorder.setAudioSource(AudioSource.MIC)
    recorder.setOutputFormat(OutputFormat.THREE_GPP)
    recorder.setAudioEncoder(AudioEncoder.AMR_NB)
    recorder.setOutputFile(storage_path)
    recorder.prepare()

class RecorderApp(App):
    is_recording = False
    encoding = ObjectProperty()

    def begin_end_recording(self):
        if self.is_recording == True:
            recorder.stop()
            recorder.reset()
            self.is_recording = False
            self.root.encoding.text = ('[font=Modern Pictograms][size=120]''e[/size][/font] \n Begin recording')
            #self.root.ids.begin_end_recording.text = ('[font=Modern Pictograms][size=120]''e[/size][/font] \n Begin recording')
        else:
            init_recorder()
            recorder.start()
            self.is_recording = True
            self.root.encoding.text = '[font=Modern Pictograms][size=120]''c[/size][/font] \n End recording'
            #self.root.ids.begin_end_recording.text = ('[font=Modern Pictograms][size=120]''e[/size][/font] \n End recording')

    def reset_player(self):
        if (player.isPlaying()):
            player.stop()
        player.reset()

    def restart_player(self):
        self.reset_player()
        try:
            player.setDataSource(storage_path)
            player.prepare()
            player.start()
        except:
            player.reset()

    def delete_file(self):
        self.reset_player()
        File(storage_path).delete()


if __name__ == '__main__':
    LabelBase.register(name='Modern Pictograms', fn_regular='modernpics.otf')
    RecorderApp().run()
