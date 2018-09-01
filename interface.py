import subtitles
filename=raw_input("path: ")
delay_hasten_value=int(raw_input("value: "))
target=raw_input("target file: ")

subtitles.create_sub_file(filename,delay_hasten_value,target)