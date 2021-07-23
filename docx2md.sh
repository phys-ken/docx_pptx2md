#!/bin/sh

find inputf -type d | xargs -I dir mkdir outputf/dir

find ./ -iname "*.docx" -type f | while read FILE
do
    path=${FILE#./}
    string_filename=${path##*/}
    string_filename_without_extension=${string_filename%.*}
    string_path=${path%/*}
    md_path=${string_path#input}
    md_file_name=${string_filename_without_extension}.md
    md_output_path=${md_path}/${md_file_name}

    echo "##File Info##"
    echo $path
    echo ${string_filename}
    echo ${string_filename_without_extension}
    echo ${string_path}
    echo $md_path
    echo $md_file_name
    echo "output path"
    echo $md_output_path
    echo "#############"

    pandoc .${path}  -o ./outputf/${md_output_path}
done

python pptx2md.py