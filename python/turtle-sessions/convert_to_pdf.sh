#!/bin/bash -e
# provide the input file name
input_file=$1
# input file name with pdf extension
output_file="$(realpath "${input_file%.*}.pdf")"
echo "Output file: ${output_file}"
# make sure we are in the input files path
pushd $(dirname $input_file)
# convert the file to pdf
pandoc -s --pdf-engine=weasyprint -o "$output_file" "$(basename $input_file)"
# --toc  - toc not really working in a coder dojo sheet.
popd
