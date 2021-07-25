# docxとpptxをmdに変換します

## 事前準備
* シェルスクリプトやpythonのスクリプトから、各種パッケージやソフトを呼び出します。事前準備で示すソフトが入っていないと、このコードは動作しません。
* pandocのインストール : [参考](https://qiita.com/sky_y/items/3c5c46ebd319490907e8)
* pythonのインストール
* pptx2mdのインストール
```
pip install pptx2md
```

## 使い方
* docx_pptx2md.shと同じ階層に、outputfと、inputfという名前のフォルダを作ります。
* inputfに、変換したいデータが入ったフォルダを保存します。
* docx_pptx2md.shを実行すれば、フォルダ構造を保ったまま、outputfに出力されます。

## 処理の詳細
* シェルスクリプトでinputfのフォルダ構造をoutputfに複製します。
* パスを受けて、pandocでwordをmdに変換します。
* imgの出力に癖がある([参考](https://stackoverflow.com/questions/39956497/pandoc-convert-docx-to-markdown-with-embedded-images))ので、以下の手順でPythonで解決しました。
  * 画像出力専用のフォルダを作る。
  * replace_path.pyをシェルスクリプトから呼び出し、作成したmdの相対パスを修正する。
  * 画像のサイズ指定のタグが中途半端に残ってしまうので、replace_path.pyで取っちゃう。
* pptxをmdに直すのは、全く別の処理になります。pptx2md.pyで、フォルダをos.walkしながら、すでにあるoutputfにデータを書き出します。


## 参考にしたサイト
* [Pandoc+シェルスクリプトでマークダウンファイルをHTMLに一括変換する方法](https://www.infoscoop.org/blogjp/2015/03/13/markdown-to-html-with-pandoc/)
  * シェルスクリプトはほぼこの通りです。
* [pptx2md](https://github.com/ssine/pptx2md)
  * かなり便利なソフト
  * くだらない操作ミスでerrorを吐かれた時も、[作者のssineさん](https://github.com/ssine/pptx2md)にissuesで質問したら、早速回答してくださいました。Thank you!

## おまけ
* enToJa.pyは、昔使ったpptxを日本語に翻訳するプログラムです。うろ覚えですが、とりあえず配布します。
* [Pythonでパワポスライドを自動翻訳する](https://qiita.com/code_440/items/9998d97b480db82ef738)