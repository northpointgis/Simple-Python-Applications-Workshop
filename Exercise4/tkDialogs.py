import tkFileDialog

def browse_file():

        file_path = tkFileDialog.askopenfile()

        if file_path:

           return file_path.name

        else:
             return

def browse_folder():

    folder_path = tkFileDialog.askdirectory()

    return folder_path
