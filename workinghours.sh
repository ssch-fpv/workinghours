#!/bin/bash
file=timetable.csv
output_file=timetable_final.csv
echo $(date '+%Y-%m-%d') $(date '+%T') >> $file

num_of_lines=$(< "$file" wc -l)

#echo $num_of_lines

if [[ $num_of_lines -eq 2 ]]
then
    start_time=$(head -n 1 "$file")
    end_time=$(tail -n 1 "$file")
    echo $start_time, $end_time >> $output_file
    rm $file
else
    echo "Do you like coffee?"
fi


python workinghours.py