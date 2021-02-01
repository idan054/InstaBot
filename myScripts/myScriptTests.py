import shutil

files_name = "2021-01-30_22-05-44_UTC"
order_ReadyPost = "2021-01-30_22-05-44_UTC"
shutil.move(f"../ThePost/{files_name}.jpg", f"../ReadyPosts/{order_ReadyPost}.jpg")