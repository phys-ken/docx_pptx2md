# docxとpptxをmdに変換します

## 事前準備
* pandocのインストール : [参考](https://qiita.com/sky_y/items/3c5c46ebd319490907e8)
* pythonのインストール
* pptx2mdのインストール
```
pip install pptx2md
```

## 使い方
* docx2md.shと同じ階層に、outputfと、inputfという名前のフォルダを作ります。
* inputfに、変換したいデータが入ったフォルダを保存します。
* docx2mdを実行すれば、フォルダ構造を保ったまま、outputfに出力されます。



## 参考にしたサイト
* [Pandoc+シェルスクリプトでマークダウンファイルをHTMLに一括変換する方法](https://www.infoscoop.org/blogjp/2015/03/13/markdown-to-html-with-pandoc/)
  * シェルスクリプトはほぼこの通りです。
* [pptx2md](https://github.com/ssine/pptx2md)
  * かなり便利なソフト

## おまけ
* enToJa.pyは、昔使ったpptxを日本語に翻訳するプログラムです。とりあえず入れておく。