import time
import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from tkinter.font import BOLD

import moviepy.editor as movie

audiofile =''
videofile =''

class AVMerge:
    def askaudio(self):                                         # For asking audiofile
        global audiofile
        audiofile = filedialog.askopenfilename()
        if (len(audiofile)>1):
            Audio_Msg.config(text=audiofile,fg="green")
        else:
            Audio_Msg.config(text="You didn't choose any file",fg="red")
        
        return audiofile

    def askvideo(self):                                         # For asking videofile
        global videofile
        videofile = filedialog.askopenfilename()
        if (len(videofile)>1):
            Video_Msg.config(text=videofile,fg="green")
        else:
            Video_Msg.config(text="You didn't choose any file",fg="red")
        return videofile


M = AVMerge()

def Merge():
    try:
        print(videofile)
        videoclip = movie.VideoFileClip(videofile)
        audioclip = movie.AudioFileClip(audiofile)
        frameRate = videoclip.fps
        print(frameRate)

    

    
        filename = videofile.split("/")
        print(filename)
        output = f"[Merged] {filename[-1]}" 
        print(output)

        newvideo = videoclip.set_audio(audioclip)
        newvideo.write_videofile(output,fps=60)
        print(newvideo.fps)

        time.sleep(1)
        tkinter.messagebox.showinfo("Message","Merge Complete!")
    except Exception as e:
        print(e)
        tkinter.messagebox.showerror("Error",e)

        




root= Tk()
root.configure(background="lightgreen")
root.title("Merge Audio and Video using moviepy")
root.geometry("500x500")

Title = Label(root,text="MERGE AUDIO AND VIDEO",bg="lightgreen",fg="black",font=("josh",15))
Title.pack(padx=20)

Select_Audio = Button(root,text="Select the Audio",bg="white",fg="blue",command=M.askaudio)
Select_Audio.pack(padx=20,pady=20)

Audio_Msg = Label(root,text="Please Select an Audio",fg="black",bg="lightgreen",font=("josh",10))
Audio_Msg.pack(padx=20,pady=10)


Video = Button(root,text="Select the Video",bg="white",fg="blue",command=M.askvideo)
Video.pack(padx=20,pady=20)

Video_Msg = Label(root,text="Please Select Video",fg="black",bg="lightgreen",font=("josh",10))
Video_Msg.pack(padx=20,pady=10)


Merge = Button(root,text="Merge Now",bg="orange",fg="black",font=("josh",10,BOLD),command=Merge)
Merge.pack(padx=20,pady=20)

root.mainloop()
