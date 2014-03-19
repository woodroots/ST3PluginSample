import sublime, sublime_plugin #必ず必要

#選択範囲をstrongで囲む
class txtWrapCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        start = "<strong>"
        end = "</strong>"

        #ST3は複数箇所の選択ができるので、forになります
        for region in self.view.sel():
                if not region.empty():
                    self.view.replace(edit, region, start + self.view.substr(region) + end)


#カーソル位置にbr挿入
class txtInsertCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
        	#選択している場所ではないのでinsertになります
            self.view.insert(edit, region.a, '<br />'+"\n")


#画像サイズを入力したら指定サイズのダミー画像を挿入
#コンソールを表示させるクラス
class imageSettingCommand(sublime_plugin.TextCommand):
    def on_done(self,arr):
        size = arr.split('x')
        w = size[0]
        h = size[1]
        self.view.run_command('insert_image', {'arr': [w,h]})

    def run(self, edit):
        self.view.window().show_input_panel('サイズを「幅x高さ」で入力（例：600x300)', '600x300', self.on_done, None, None)

#実際に行われる処理
class insertImage(sublime_plugin.TextCommand):
    def run(self,edit,arr):
        w = arr[0]
        h = arr[1]

        img = '<img src="http://placehold.jp/WIDTHxHEIGHT.png" width="WIDTH" height="HEIGHT" alt="">'

        img = img.replace('WIDTH',w)
        img = img.replace('HEIGHT',h)

        for region in self.view.sel():
            self.view.insert(edit, region.a, img)