import os
import csv

current_directory = os.getcwd()


class DataController():
    def _load_array_of_content(self, filename):
        content = []
        with open(filename, 'r') as station_machine:
            c = csv.reader(station_machine, delimiter='\t', skipinitialspace=True)
            for line in c:
                content.append(line)
        return content

    station_1_queue_contents = _load_array_of_content([], 'd:/test/s1q.xls')
    station_1_utilization_contents = _load_array_of_content([], 'd:/test/s1u.xls')
    station_2_queue_contents = _load_array_of_content([], 'd:/test/s2q.xls')
    station_2_utilization_contents = _load_array_of_content([], 'd:/test/s2u.xls')
    station_3_queue_contents = _load_array_of_content([], 'd:/test/s3q.xls')
    station_3_utilization_contents = _load_array_of_content([], 'd:/test/s3u.xls')

    station_1_queue_contents[0][1] = 'S1Q'
    station_2_queue_contents[0][1] = 'S2Q'
    station_3_queue_contents[0][1] = 'S3Q'
    station_1_utilization_contents[0][1] = 'S1U'
    station_2_utilization_contents[0][1] = 'S2U'
    station_3_utilization_contents[0][1] = 'S3U'
    with open('d:/test/summary.xls', 'w') as little_field_summary:
        for index in range(len(station_1_queue_contents)):
            little_field_summary.write(station_1_queue_contents[index][0])
            little_field_summary.write('\t')

            little_field_summary.write(station_1_queue_contents[index][1])
            little_field_summary.write('\t')
            little_field_summary.write(station_1_utilization_contents[index][1])
            little_field_summary.write('\t')

            little_field_summary.write(station_2_queue_contents[index][1])
            little_field_summary.write('\t')
            little_field_summary.write(station_2_utilization_contents[index][1])
            little_field_summary.write('\t')

            little_field_summary.write(station_3_queue_contents[index][1])
            little_field_summary.write('\t')
            little_field_summary.write(station_3_utilization_contents[index][1])
            little_field_summary.write('\t')

            little_field_summary.write('\n')



