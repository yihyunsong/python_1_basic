txt_file = open("save.txt", 'w', newline='')
temp = '''
Hi my name is minsoo
Hello python
I like animals
'''
txt_file.write(temp)

txt_file.close()