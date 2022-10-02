''' Creation Date: 02/10/2022 '''


import speech_recognition as sr
import static_ffmpeg
import os


static_ffmpeg.add_paths()


def user_input():
    ''' Returns: User selected filename and extension from Files folder. '''
    while True:
        file = input('Enter filename: ')
        filename, extension = os.path.splitext(file)
        if filename and extension != '':
            return filename, extension
        print('Invalid, provide name and extension of file from Files folder...')
        continue


def convert_to_wav(filename: str, extension: str):
    ''' Purpose: Converts selected audio/video file to .wav file. '''
    try:
        if os.path.exists(f'Files/{filename}.wav'):
            print('Using existing .wav file')
        else:
            os.system(f'ffmpeg -i Files/{filename}{extension} Files/{filename}.wav')
    except Exception as e:
        print(f'File .wav conversion failed:\n{e}')


def transcribe(filename: str, extension: str):
    ''' Purpose: Print transcription of audio/video file. '''
    filename = filename.removesuffix(extension)
    convert_to_wav(filename, extension)
    r = sr.Recognizer()
    with sr.AudioFile(f'Files/{filename}.wav') as source:
        audio = r.record(source) # read audio file                  
        print(f'Transcription: {r.recognize_google(audio)}')


if __name__ == '__main__':
    filename, extension = user_input()
    transcribe(filename, extension)
        